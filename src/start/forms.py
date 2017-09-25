__author__ = 'NeroS'
from django import forms
from .models import (Mensaje, Equipo, Categoria, Slideshow, Marca,
                     Departamento, Familia)


class RegEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['categoria', 'clave', 'nombre', 'modelo', 'marca',
                  'linea', 'familia', 'top_vendido', 'promo', 'nuevo', 'precio',
                  'descripcion', 'imagen', 'imagen_1', 'imagen_2', 'imagen_3']

    def __init__(self, *args, **kwargs):
        super(RegEquipoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].label = 'Categoría'
        self.fields['categoria'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Categoría',
        })
        self.fields['clave'].label = 'Clave'
        self.fields['clave'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Clave',
        })
        self.fields['nombre'].label = 'Nombre'
        self.fields['nombre'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Nombre',
        })
        self.fields['modelo'].label = 'Modelo'
        self.fields['modelo'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Modelo',
        })
        self.fields['linea'].label = 'Línea'
        self.fields['linea'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Línea',
        })
        self.fields['precio'].label = 'Precio'
        self.fields['precio'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Precio',
        })
        self.fields['top_vendido'].label = 'Más vendido'
        self.fields['promo'].label = 'En promoción'
        self.fields['nuevo'].label = 'Producto nuevo'

        self.fields['descripcion'].label = 'Descripción'
        self.fields['descripcion'].widget.attrs.update({
            'placeholder': 'Descripción',
        })
        self.fields['imagen'].label = 'Imagen principal'
        self.fields['imagen_1'].label = 'Imagen secundaria'
        self.fields['imagen_2'].label = 'Imagen secundaria'
        self.fields['imagen_3'].label = 'Imagen secundaria'

class RegMarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']
    def __init__(self, *args, **kwargs):
        super(RegMarcaForm, self).__init__(*args, **kwargs)
        self.fields['marca'].label = ''
        self.fields['marca'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Marca',
        })


class RegFamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['familia']
    def __init__(self, *args, **kwargs):
        super(RegFamiliaForm, self).__init__(*args, **kwargs)
        self.fields['familia'].label = ''
        self.fields['familia'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Familia',
        })

class RegSlideshowForm(forms.ModelForm):
    class Meta:
        model = Slideshow
        fields = ['titulo', 'descripcion', 'imagen']

    def __init__(self, *args, **kwargs):
        super(RegSlideshowForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].label = ''
        self.fields['titulo'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Título',
        })
        self.fields['descripcion'].label = ''
        self.fields['descripcion'].widget.attrs.update({
            'placeholder': 'Descripción',
        })



class RegCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria', 'departamento']

    def __init__(self, *args, **kwargs):
        super(RegCategoriaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].label = ''
        self.fields['categoria'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Categoría',
        })
        self.fields['departamento'].label = 'Departamento'
        self.fields['departamento'].widget.attrs.update({
            'placeholder': 'Departamento',
        })

class RegDepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['departamento']

    def __init__(self, *args, **kwargs):
        super(RegDepartamentoForm, self).__init__(*args, **kwargs)
        self.fields['departamento'].label = ''
        self.fields['departamento'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Departamento',
        })

class RegContactForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']

    def __init__(self, *args, **kwargs):
        super(RegContactForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = ''
        self.fields['nombre'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Nombre',
        })
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'placeholder': 'Email',
        })
        self.fields['telefono'].label = ''
        self.fields['telefono'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Teléfono',
        })
        self.fields['mensaje'].label = ''
        self.fields['mensaje'].widget.attrs.update({
            'placeholder': 'Mensaje',
        })
