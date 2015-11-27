from django.shortcuts import render
from django.utils import timezone
from .models import Movil

# Create your views here.
def post_list(request):
        moviles = Movil.objects.filter(fecha_lanzamiento__lte=timezone.now()).order_by('fecha_lanzamiento')
        return render(request, 'app1/post_list.html',{'moviles': moviles})
