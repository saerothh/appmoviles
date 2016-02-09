
'''
#Añadir nuevo movil
@login_required(login_url='ingresar')
def movil_new(request):
#    if request.user.is_authenticated() and request.user.has_perm('moviles.add_movil'):
	if request.method == "POST":
		formulario = MovilForm(request.POST)
		valorform = ValoracionForm()
		if formulario.is_valid():
				movil = formulario.save()
				valorform = formulario.save(commit=False)
				valoracion.movil = movil
				valoracion.save()
				return redirect('moviles.views.movil_detail', pk=movil.pk)
	else:
		formulario = MovilForm()
		valorform = ValoracionForm()
#    else:
#       return HttpResponse("No tienes permisos para realizar esta acción.")
	return render (request, 'moviles/movil_edit.html', {'formulario': formulario, 'valorform': valorform})


#Modificar movil ya añadido
@login_required(login_url='ingresar')
def movil_new(request):
	if request.method == "POST":
		movil_form = MovilForm(request.POST, instance = Movil())
#		valoracion_form = ValoracionForm(request.POST, instance = Valoracion())
		if movil_form.is_valid() and valoracion_form.is_valid():
			movil = movil_form.save(commit=False)
			movil.usuario = request.user
			movil.save()
			movil_form.save()
#			valoracion_form.save()
			return HttpResponseRedirect('/')
	else:
		movil_form = MovilForm()
#		valoracion_form = ValoracionForm()
	return render_to_response('moviles/movil_edit.html', {'movil_form': movil_form, valoracion_form': valoracion_form'}, context_instance= RequestContext(request))


@login_required(login_url='ingresar')
def movil_edit(request, pk):
#    if request.user.is_authenticated() and request.user.has_perm('moviles.add_movil'):
	movil = get_object_or_404(Movil, pk=pk)
	if request.method == "POST":
		formulario = MovilForm(request.POST, instance=movil)
		if formulario.is_valid():
			movil=formulario.save()
			return redirect('moviles.views.movil_detail', pk=movil.pk)
	else:
		formulario = MovilForm(instance=movil)
#    else:
#       return HttpResponse("No tienes permisos para realizar esta acción.")
	return render(request, 'moviles/movil_edit.html', {'formulario': formulario})

'''


'''
#Eliminar un movil
@login_required(login_url='ingresar')
def movil_remove(request, pk):
#	if request.user.is_authenticated() and request.user.has_perm('moviles.delete_movil'):
	movil = get_object_or_404(Movil, pk=pk)
	movil.delete()
#	else:
#		return HttpResponse("No tienes permisos para realizar esta acción.")
	return redirect('moviles.views.movil_list')
'''

