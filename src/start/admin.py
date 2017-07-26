from django.contrib import admin
from .models import (Mensaje, Equipo, Categoria, Slideshow, Slideshow_marcas, Marca, Procesador,
                     SistemaOperativo, DiscoDuro, Ram, Departamento)
from .forms import (RegContactForm, RegEquipoForm, RegCategoriaForm, RegMarcaForm,
                    RegSistemaOperativoForm, RegSlideshowForm, RegSlideshowMarcasForm,
                    RegProcesadorForm, RegDiscoDuroForm, RegRamForm, RegDepartamentoForm)


class AdminEquipo(admin.ModelAdmin):
    list_display = ['categoria_categoria', 'nombre', 'modelo', 'marca_marca', 'timestamp']
    form = RegEquipoForm
    list_display_links = ['nombre']
    list_filter = ['timestamp']
    list_editable = ['modelo']
    search_fields = ['nombre', 'modelo', 'marca']

    def categoria_categoria(self, obj):
        return obj.categoria.categoria

    def marca_marca(self, obj):
        return obj.marca.marca

    categoria_categoria.short_description = 'Categoria'
    marca_marca.short_description = 'Marca'


class AdminMarca(admin.ModelAdmin):
    list_display = ['marca']
    form = RegMarcaForm
    list_display_links = ['marca']
    search_fields = ['marca']


class AdminSistemaOperativo(admin.ModelAdmin):
    list_display = ['sistema_operativo']
    form = RegSistemaOperativoForm
    list_display_links = ['sistema_operativo']


class AdminProcesador(admin.ModelAdmin):
    list_display = ['procesador']
    form = RegProcesadorForm
    list_display_links = ['procesador']


class AdminDiscoDuro(admin.ModelAdmin):
    list_display = ['disco_duro']
    form = RegDiscoDuroForm
    list_display_links = ['disco_duro']


class AdminRam(admin.ModelAdmin):
    list_display = ['ram']
    form = RegRamForm
    list_display_links = ['ram']


class AdminSlideshow(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']
    form = RegSlideshowForm
    list_editable = ['descripcion']
    search_fields = ['titulo', 'descripcion']


class AdminSlideshowMarcas(admin.ModelAdmin):
    list_display = ['titulo']
    form = RegSlideshowMarcasForm
    search_fields = ['titulo']

    def equipo_nombre(self, obj):
        return obj.titulo


class AdminContacto(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'timestamp']
    form = RegContactForm
    list_filter = ['timestamp']
    list_editable = ['nombre']
    search_fields = ['email', 'nombre']


class AdminCategoria(admin.ModelAdmin):
    list_display = ['categoria']
    form = RegCategoriaForm
    #  list_edtiable = ['categoria']
    search_fields = ['categoria']


class AdminDepartamento(admin.ModelAdmin):
    list_display = ['departamento']
    form = RegDepartamentoForm
    list_display_links = ['departamento']
    search_fields = ['departamento']


admin.site.register(Mensaje, AdminContacto)
admin.site.register(Equipo, AdminEquipo)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Slideshow, AdminSlideshow)
admin.site.register(Slideshow_marcas, AdminSlideshowMarcas)
admin.site.register(Marca, AdminMarca)
admin.site.register(SistemaOperativo, AdminSistemaOperativo)
admin.site.register(Procesador, AdminProcesador)
admin.site.register(DiscoDuro, AdminDiscoDuro)
admin.site.register(Ram, AdminRam)
admin.site.register(Departamento, AdminDepartamento)
