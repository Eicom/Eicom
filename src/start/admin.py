from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Mensaje, Equipo, Categoria, Slideshow
from .forms import RegContactForm, RegEquipoForm, RegCategoriaForm, RegSlideshowForm

class AdminEquipo(admin.ModelAdmin):
    list_display = ['categoria_categoria', 'nombre', 'modelo', 'marca', 'timestamp']
=======
from .models import Mensaje,Equipo, Categoria
from .forms import RegContactForm, RegEquipoForm, RegCategoriaForm

class AdminEquipo(admin.ModelAdmin):
    list_display = ['categoria_categoria','nombre', 'modelo', 'marca', 'timestamp']
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
    form = RegEquipoForm
    list_display_links = ['nombre']
    list_filter = ['timestamp']
    list_editable = ['modelo']
    search_fields = ['nombre', 'modelo', 'marca']

    def categoria_categoria(self,obj):
        return obj.categoria.categoria
    categoria_categoria.short_description = 'Categoria'

<<<<<<< HEAD
class AdminSlideshow(admin.ModelAdmin):
	list_display = ['titulo','descripcion','equipo_nombre']
	form = RegSlideshowForm
	list_editable = ['descripcion']
	search_fields = ['titulo','descripcion']

	def equipo_nombre(self,obj):
		return obj.equipo

	equipo_nombre.short_descripcion = 'Equipo'

=======
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
class AdminContacto(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'timestamp']
    form = RegContactForm
    list_filter = ['timestamp']
    list_editable = ['nombre']
    search_fields = ['email', 'nombre']

class AdminCategoria(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['categoria']
    form = RegCategoriaForm
    #list_editable = ['categoria']
    search_fields = ['categoria']

=======
	list_display = ['categoria']
	form = RegCategoriaForm
	list_edtiable = ['categoria']
	search_fields = ['categoria']
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f

admin.site.register(Mensaje, AdminContacto)
admin.site.register(Equipo, AdminEquipo)
admin.site.register(Categoria, AdminCategoria)
<<<<<<< HEAD
admin.site.register(Slideshow, AdminSlideshow)
=======
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
