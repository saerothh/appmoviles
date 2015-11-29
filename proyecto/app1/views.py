from django.shortcuts import render
from django.utils import timezone
from .models import Movil
from django.shortcuts import render, get_object_or_404

# Create your views here.
def movil_list(request):
        moviles = Movil.objects.filter(fecha_lanzamiento__lte=timezone.now()).order_by('fecha_lanzamiento')
        return render(request, 'app1/movil_list.html',{'moviles': moviles})

def movil_detail(request, pk):
        moviles = get_object_or_404(Movil, pk=pk)
        return render(request, 'app1/movil_detail.html', {'Movil': moviles})
