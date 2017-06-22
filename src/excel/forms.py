from django import forms
from .models import Producto


class RegProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['clave', 'descripcion', 'unidad', 'marca', 'modelo',
                  'linea', 'familia', 'divisa', 'precio_pub', 'imagen']
