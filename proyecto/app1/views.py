from django.utils import timezone
from .models import Movil
from .forms import MovilForm
from django.shortcuts import redirect, render_to_response, render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect


# Create your views here.
def movil_list(request):
    moviles = Movil.objects.filter(fecha_lanzamiento__lte=timezone.now()).order_by('fecha_lanzamiento')
    return render(request, 'app1/movil_list.html',{'moviles': moviles})

def movil_detail(request, pk):
        movil = get_object_or_404(Movil, pk=pk)
        return render(request, 'app1/movil_detail.html', {'Movil': movil})

@login_required
def movil_new(request):
    if request.user.is_authenticated() and request.user.has_perm('app1.add_movil'):
      if request.method == "POST":
         form = MovilForm(request.POST)
         if form.is_valid():
            movil = form.save()
            return redirect('app1.views.movil_detail', pk=movil.pk)
      else:
         form = MovilForm()
    else:
       return HttpResponse("No tienes permiso para crear elementos.")
    return render (request, 'app1/movil_edit.html', {'form': form})

@login_required
def movil_edit(request, pk):
    if request.user.is_authenticated() and request.user.has_perm('app1.add_movil'):
      movil = get_object_or_404(Movil, pk=pk)
      if request.method == "POST":
          form = MovilForm(request.POST, instance=movil)
          if form.is_valid():
              movil=form.save()
              return redirect('app1.views.movil_detail', pk=movil.pk)
      else:
          form = MovilForm(instance=movil)
    else:
       return HttpResponse("No tienes permiso para editar elementos.")
    return render(request, 'app1/movil_edit.html', {'form': form})

@login_required
def movil_remove(request, pk):
    if request.user.is_authenticated() and request.user.has_perm('app1.delete_movil'):
      movil = get_object_or_404(Movil, pk=pk)
      movil.delete()
    else:
       return HttpResponse("No tienes permiso para eliminar elementos.")
    return redirect('app1.views.movil_list')

"""
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("Ha habido un error")
    else:
        data, errors = {}, {}

    return render_to_response("registration/register.html", {
        'form' : forms.FormWrapper(form, data, errors)
    })
"""
