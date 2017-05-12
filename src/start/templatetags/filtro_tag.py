from django import template
from start.models import Categoria

register = template.Library()

@register.assignment_tag
def categorias_lista():
	return Categoria.objects.all()
