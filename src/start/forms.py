__author__ = 'NeroS'
# -*- coding: utf-8 -*-

from django import forms
# from crispy_forms.bootstrap import AppendedText, PrependedText
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, ButtonHolder, Submit
# from crispy_forms.layout import Field
from .models import Mensaje, Equipo, Categoria

class RegEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['categoria','nombre', 'modelo', 'marca','so', 'procesador',
                  'harddrive', 'pantalla', 'ram', 'video',
                  'precio', 'imagen']

class RegCategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['categoria']

class RegContactForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'telefono', 'tema', 'mensaje']
    def __init__(self, *args, **kwargs):
        super(RegContactForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput, forms.EmailInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label + ':'})
            field.label = ""
        # self.fields["nombre"].label = ""



