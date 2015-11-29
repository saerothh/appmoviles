from django.utils import timezone
from .models import Movil
from django.shortcuts import render, get_object_or_404
from .forms import MovilForm
from django.shortcuts import redirect


# Create your views here.
def movil_list(request):
        moviles = Movil.objects.filter(fecha_lanzamiento__lte=timezone.now()).order_by('fecha_lanzamiento')
        return render(request, 'app1/movil_list.html',{'moviles': moviles})

def movil_detail(request, pk):
        movil = get_object_or_404(Movil, pk=pk)
        return render(request, 'app1/movil_detail.html', {'Movil': movil})

def movil_new(request):
    if request.method == "POST":
        form = MovilForm(request.POST)
        if form.is_valid():
           movil = form.save()
           return redirect('app1.views.movil_detail', pk=movil.pk)
    else:
        form = MovilForm()
    return render (request, 'app1/movil_edit.html', {'form': form})

def movil_edit(request, pk):
        movil = get_object_or_404(Movil, pk=pk)
        if request.method == "POST":
            form = MovilForm(request.POST, instance=movil)
            if form.is_valid():
                movil=form.save()
                return redirect('app1.views.movil_detail', pk=movil.pk)
        else:
            form = MovilForm(instance=movil)
        return render(request, 'app1/movil_edit.html', {'form': form})
