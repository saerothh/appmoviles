from django import forms
from .models import Movil, Comentario, Valoracion
from django.forms import ModelForm



class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class MovilForm(forms.ModelForm):
	class Meta:
		model = Movil
		exclude = ['usuario', 'valoraciones']

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ('texto',)

class ValoracionForm(forms.ModelForm):
	class Meta:
		model = Valoracion
		fields = ('valoracion',)
