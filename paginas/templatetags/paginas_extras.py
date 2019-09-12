from django import template
from paginas.models import Pagina

register  = template.Library()

@register.simple_tag
def get_pagina_list():
	paginas = Pagina.objects.all()
	return paginas