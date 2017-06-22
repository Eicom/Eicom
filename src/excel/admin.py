from django.contrib import admin
from .models import Question, Choice, Producto
from .forms import RegProductoForm


class AdminProducto(admin.ModelAdmin):
    list_display = ['clave', 'descripcion', 'marca',
                    'linea', 'familia', 'divisa', 'precio_pub']
    form = RegProductoForm
    list_display_links = ['clave']
    list_filter = ['familia']
    list_editable = ['descripcion']
    search_fields = ['clave', 'descripcion', 'marca', 'linea', 'familia']

    # def familia(self, obj):
    #     return obj.familia.familia
    # familia.short_description = 'Familia'


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Producto, AdminProducto)
