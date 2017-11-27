from django import template
from start.models import Categoria, Departamento, Equipo

register = template.Library()


@register.assignment_tag
def categorias_lista():
    return Categoria.objects.all()


@register.assignment_tag
def departamento_lista():
    return Departamento.objects.all()

@register.assignment_tag
def top_lista():
    return Equipo.objects.filter(top_vendido__icontains=1)

@register.assignment_tag
def promo_lista():
    return Equipo.objects.filter(promo__icontains=1)
