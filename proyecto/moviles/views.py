from django.utils import timezone
from .models import Movil, Comentario, Valoracion, User
from .forms import MovilForm, ComentarioForm, ValoracionForm
from django.shortcuts import redirect, render_to_response, render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django import forms
from django.http import HttpResponseRedirect
from django.template import loader, RequestContext
from random import sample

#Inicio
def inicio(request):
	usuario = request.user
	if usuario.is_authenticated():
		return redirect('lista_ordenada')
	else: 
		return redirect('lista_aleatoria')


@login_required(login_url='ingresar')
#Lista de moviles ordenadas por fecha de lanzamiento
def movil_list(request):
	usuario = request.user
	moviles = Movil.objects.filter(fecha_lanzamiento__lte=timezone.now()).order_by('fecha_lanzamiento')
	return render(request, 'moviles/movil_list.html',{'moviles': moviles, 'Usuario':usuario})


#Lista de de moviles aleatoria
def movil_list_random(request):
	moviles = Movil.objects.filter()
	#Para listas aleatorias
	moviles = sample(list(moviles), 9)
	return render(request, 'moviles/movil_list_random.html',{'moviles': moviles})


#Detalles movil creados
def movil_detail(request, pk):
	movil = get_object_or_404(Movil, pk=pk)
	comentarios = Comentario.objects.filter(movil= movil)
	try:
		valoraciones= Valoracion.objects.filter(movil= movil, usuario= request.user)
		valormovil = get_object_or_404(Valoracion, pk= valoraciones)
		return render(request, 'moviles/movil_detail.html',{'Movil': movil,'Comentarios': comentarios, 'Valoracion': valormovil, 'Usuario':request.user})
	except:
		return render(request, 'moviles/movil_detail.html',{'Movil': movil,'Comentarios': comentarios, 'Usuario':request.user})


#Creacion de nuevo usuario
def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect('access')
	else:
		formulario = UserCreationForm()
	return render_to_response('moviles/user_new.html', {'formulario': formulario}, context_instance=RequestContext(request))

#Ingreso de usuario
def ingresar(request):
	if not request.user.is_anonymous():
		return redirect('lista_ordenada')
	if request.method=='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return redirect('lista_ordenada')
				else:
					return render_to_response('moviles/no_active.html', context_instance=RequestContext(request))
			else:
				return render_to_response('moviles/no_user.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('moviles/access.html',{'formulario':formulario}, context_instance=RequestContext(request))

#Cierre de sesion
@login_required(login_url='ingresar')
def cerrar(request):
	logout(request)
	return redirect('lista_aleatoria')

#Nuevo comentario
def nuevo_comentario(request, pk):
	usuario = request.user
	movil = Movil.objects.get(id=pk)
	if request.method=='POST':
		formulario = ComentarioForm(request.POST)
		if formulario.is_valid():
			comentario = formulario.save(commit=False)
			comentario.movil = movil
			comentario.nombre = usuario
			comentario.save()
			return redirect('moviles.views.movil_detail', pk)
	else:
		formulario = ComentarioForm()
	return render_to_response('moviles/comment.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='ingresar')
#Cambiar valoracion
def editar_valoracion(request, pk):
	usuario = request.user
	valor = Valoracion.objects.get(id=pk)
	if request.method=='POST':
		formulario = ValoracionForm(request.POST, instance=valor)
		if formulario.is_valid():
			formulario.save()
			return redirect('/')
	else:
		formulario = ValoracionForm()
	return render_to_response('moviles/val_edit.html',{'formulario':formulario, 'Usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='ingresar')
#Nueva valoracion
def crear_valoracion(request, pk):
	usuario = request.user
	movil = Movil.objects.get(id=pk)
	if request.method=='POST':
		formulario = ValoracionForm(request.POST)
		if formulario.is_valid():
			valoracion = formulario.save(commit=False)
			valoracion.movil = movil
			valoracion.usuario = usuario
			valoracion.save()
			return redirect('/')
	else:
		formulario = ValoracionForm()
	return render_to_response('moviles/val_edit.html',{'formulario':formulario, 'Usuario':usuario}, context_instance=RequestContext(request))
