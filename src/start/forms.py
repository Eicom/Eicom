__author__ = 'NeroS'
from django import forms
from .models import (Mensaje, Equipo, Categoria, Slideshow, Slideshow_marcas, Marca,
                     SistemaOperativo, Procesador, DiscoDuro, Ram, Departamento)


class RegEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['categoria', 'nombre', 'modelo', 'sistema_operativo', 'marca',  'procesador',
                  'disco_duro', 'pantalla', 'memoria_ram', 'tarjeta_madre', 'bateria',
                  'camara', 'adaptador_ac', 'video', 'top_vendido', 'promo', 'precio',
                  'descripcion', 'imagen', 'imagen_1', 'imagen_2', 'imagen_3']


class RegMarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']


class RegSistemaOperativoForm(forms.ModelForm):
    class Meta:
        model = SistemaOperativo
        fields = ['sistema_operativo']


class RegProcesadorForm(forms.ModelForm):
    class Meta:
        model = Procesador
        fields = ['procesador']


class RegDiscoDuroForm(forms.ModelForm):
    class Meta:
        model = DiscoDuro
        fields = ['disco_duro']


class RegRamForm(forms.ModelForm):
    class Meta:
        model = Ram
        fields = ['ram']


class RegSlideshowForm(forms.ModelForm):
    class Meta:
        model = Slideshow
        fields = ['titulo', 'descripcion', 'imagen']


class RegSlideshowMarcasForm(forms.ModelForm):
    class Meta:
        model = Slideshow_marcas
        fields = ['titulo', 'imagen']


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
