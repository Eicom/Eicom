__author__ = 'NeroS'
# -*- coding: utf-8 -*-

from django import forms
<<<<<<< HEAD
from .models import Mensaje, Equipo, Categoria, Slideshow
=======
# from crispy_forms.bootstrap import AppendedText, PrependedText
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, ButtonHolder, Submit
# from crispy_forms.layout import Field
from .models import Mensaje, Equipo, Categoria
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f

class RegEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
<<<<<<< HEAD
        fields = ['categoria', 'nombre', 'modelo', 'marca', 'so', 'procesador',
                  'harddrive', 'pantalla', 'ram', 'video', 'precio',
                  'descripcion', 'imagen']

class RegSlideshowForm(forms.ModelForm):
	class Meta:
		model = Slideshow
		fields = ['titulo','descripcion','equipo','imagen']

class RegCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']
=======
        fields = ['categoria','nombre', 'modelo', 'marca','so', 'procesador',
                  'harddrive', 'pantalla', 'ram', 'video',
                  'precio', 'imagen']

class RegCategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['categoria']
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f

class RegContactForm(forms.ModelForm):
    class Meta:
        model = Mensaje
<<<<<<< HEAD
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']
=======
        fields = ['nombre', 'email', 'telefono', 'tema', 'mensaje']
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
    def __init__(self, *args, **kwargs):
        super(RegContactForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput, forms.EmailInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label + ':'})
            field.label = ""
        # self.fields["nombre"].label = ""



