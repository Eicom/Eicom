__author__ = 'NeroS'
from django import forms
from .models import (Mensaje, Equipo, Categoria, Slideshow, Marca,
                     Departamento, Familia)


class RegEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['categoria', 'clave', 'nombre', 'modelo', 'marca',
                  'linea', 'familia', 'top_vendido', 'promo', 'precio',
                  'descripcion', 'imagen', 'imagen_1', 'imagen_2', 'imagen_3']

    def __init__(self, *args, **kwargs):
        super(RegEquipoForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.label = ''


class RegMarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']


class RegFamiliaForm(forms.ModelForm):
    class meta:
        model = Familia
        fields = ['familia']


class RegSlideshowForm(forms.ModelForm):
    class Meta:
        model = Slideshow
        fields = ['titulo', 'descripcion', 'imagen']


class RegCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria', 'departamento']


class RegDepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['departamento']


class RegContactForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']

    def __init__(self, *args, **kwargs):
        super(RegContactForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput, forms.EmailInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label + ':'})
            field.label = ""
