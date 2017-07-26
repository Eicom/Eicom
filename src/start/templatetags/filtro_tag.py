from django import template
from start.models import Categoria, Departamento

register = template.Library()


@register.assignment_tag
def categorias_lista():
    return Categoria.objects.all()


@register.assignment_tag
def departamento_lista():
    return Departamento.objects.all()
