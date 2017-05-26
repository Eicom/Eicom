<<<<<<< HEAD
from django import template
from start.models import Categoria

register = template.Library()

@register.assignment_tag
def categorias_lista():
	return Categoria.objects.all()
=======
from django import template
from start.models import Categoria

register = template.Library()

@register.assignment_tag
def categorias_lista():
	return Categoria.objects.all()
>>>>>>> a2c84bb6414900b317fa31774f5e74fdb247d49f
