from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.inicio, name ='inicio'),
	url(r'^movil/list/$', views.movil_list, name='lista_ordenada'),
	url(r'^movil/list/random/$', views.movil_list_random, name ='lista_aleatoria'),
	url(r'^movil/(?P<pk>[0-9]+)/$', views.movil_detail, name='movil_detail'),
	url(r'^usuario/new/$', views.nuevo_usuario, name ='user_new'),
	url(r'^ingresar/$', views.ingresar, name= 'access'),
	url(r'^cerrar/$', views.cerrar, name= 'close'),
	url(r'^movil/(?P<pk>[0-9]+)/comenta/$', views.nuevo_comentario, name='movil_comenta'),
	url(r'^valoracion/(?P<pk>[0-9]+)/edit/$', views.editar_valoracion, name='val_edit'),
	url(r'^valoracion/(?P<pk>[0-9]+)/crear/$', views.crear_valoracion, name='val_new'),
]
