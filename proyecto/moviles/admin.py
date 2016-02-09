from django.contrib import admin

from .models import Movil, Comentario, Valoracion

# Register your models here.
class MovilAdmin(admin.ModelAdmin):
	model = Movil
	list_display = ('nombre', 'fabricante', 'fecha_lanzamiento',)
	list_filter = ('nombre', 'fabricante')
	ordering = ('-fecha_lanzamiento',)
	search_fields = ('nombre',)
admin.site.register(Movil, MovilAdmin)

class ValoracionAdmin(admin.ModelAdmin):
	model = Valoracion
	list_display = ('movil', 'usuario', 'valoracion',)
	ordering = ('-valoracion',)
	list_filter = ('valoracion',)
	search_fields = ('usuario',)
admin.site.register(Valoracion, ValoracionAdmin)

class ComentarioAdmin(admin.ModelAdmin):
	model = Comentario
	list_display = ('nombre', 'movil', 'texto',)
	list_filter = ('nombre', 'movil',)
	ordering = ('-fecha',)
	search_fields = ('nombre',)
admin.site.register(Comentario, ComentarioAdmin)

