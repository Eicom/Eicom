from django.contrib import admin
from .models import (Mensaje, Equipo, Categoria, Slideshow, Marca, Departamento, Familia)
from .forms import (RegContactForm, RegEquipoForm, RegCategoriaForm, RegMarcaForm,
                    RegFamiliaForm, RegDepartamentoForm, RegSlideshowForm)


class AdminEquipo(admin.ModelAdmin):
    list_display = ['categoria_categoria', 'nombre', 'modelo', 'marca_marca', 'timestamp',
                    'familia_familia']
    form = RegEquipoForm
    list_display_links = ['nombre']
    list_filter = ['timestamp']
    search_fields = ['nombre', 'modelo', 'marca', 'familia_familia', 'categoria_categoria',
                     'marca_marca']

    def categoria_categoria(self, obj):
        return obj.categoria.categoria

    def marca_marca(self, obj):
        return obj.marca.marca

    def familia_familia(self, obj):
        return obj.familia.familia

    categoria_categoria.short_description = 'Categoria'
    familia_familia.short_description = 'Familia'
    marca_marca.short_description = 'Marca'


class AdminMarca(admin.ModelAdmin):
    list_display = ['marca']
    form = RegMarcaForm
    list_display_links = ['marca']
    search_fields = ['marca']


class AdminSlideshow(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']
    form = RegSlideshowForm
    list_editable = ['descripcion']
    search_fields = ['titulo', 'descripcion']


class AdminContacto(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'timestamp']
    form = RegContactForm
    list_filter = ['timestamp']
    list_editable = ['nombre']
    search_fields = ['email', 'nombre']


class AdminCategoria(admin.ModelAdmin):
    list_display = ['categoria']
    form = RegCategoriaForm
    search_fields = ['categoria']


class AdminDepartamento(admin.ModelAdmin):
    list_display = ['departamento']
    form = RegDepartamentoForm
    list_display_links = ['departamento']
    search_fields = ['departamento']


class AdminFamilia(admin.ModelAdmin):
    list_display = ['familia']
    form = RegFamiliaForm
    list_display_links = ['familia']
    search_fields = ['familia']


admin.site.register(Mensaje, AdminContacto)
admin.site.register(Equipo, AdminEquipo)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Slideshow, AdminSlideshow)
admin.site.register(Marca, AdminMarca)
admin.site.register(Departamento, AdminDepartamento)
admin.site.register(Familia, AdminFamilia)
