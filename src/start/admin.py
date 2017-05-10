from django.contrib import admin

# Register your models here.
from .models import Mensaje,Equipo
from .forms import RegContactForm, RegEquipoForm

class AdminEquipo(admin.ModelAdmin):
    list_display = ['clasificacion', 'nombre', 'modelo', 'marca', 'timestamp']
    form = RegEquipoForm
    list_display_links = ['nombre']
    list_filter = ['timestamp']
    list_editable = ['modelo']
    search_fields = ['clasificacion', 'nombre', 'modelo', 'marca']

class AdminContacto(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'timestamp']
    form = RegContactForm
    list_filter = ['timestamp']
    list_editable = ['nombre']
    search_fields = ['email', 'nombre']

admin.site.register(Mensaje, AdminContacto)
admin.site.register(Equipo, AdminEquipo)
