from django import forms

from .models import Movil

class MovilForm(forms.ModelForm):

 class Meta:
     model = Movil
     fields = ('modelo', 'fecha_lanzamiento',)
