from django.contrib import admin

# Register your models here.
from .models import Mensaje, Equipo, Categoria, Slideshow
from .forms import RegContactForm, RegEquipoForm, RegCategoriaForm, RegSlideshowForm

class AdminEquipo(admin.ModelAdmin):
    list_display = ['categoria_categoria', 'nombre', 'modelo', 'marca', 'timestamp']
    form = RegEquipoForm
    list_display_links = ['nombre']
    list_filter = ['timestamp']
    list_editable = ['modelo']
    search_fields = ['nombre', 'modelo', 'marca']

    def categoria_categoria(self,obj):
        return obj.categoria.categoria
    categoria_categoria.short_description = 'Categoria'

class AdminSlideshow(admin.ModelAdmin):
	list_display = ['titulo','descripcion','equipo_nombre']
	form = RegSlideshowForm
	list_editable = ['descripcion']
	search_fields = ['titulo','descripcion']

	def equipo_nombre(self,obj):
		return obj.equipo

	equipo_nombre.short_descripcion = 'Equipo'

class AdminContacto(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'timestamp']
    form = RegContactForm
    list_filter = ['timestamp']
    list_editable = ['nombre']
    search_fields = ['email', 'nombre']

class AdminCategoria(admin.ModelAdmin):
    list_display = ['categoria']
    form = RegCategoriaForm
    #list_editable = ['categoria']
    search_fields = ['categoria']


admin.site.register(Mensaje, AdminContacto)
admin.site.register(Equipo, AdminEquipo)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Slideshow, AdminSlideshow)
