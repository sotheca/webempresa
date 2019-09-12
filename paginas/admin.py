from django.contrib import admin
from .models import Pagina


# Register your models here.
class PaginaAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('title','orden')

admin.site.register(Pagina, PaginaAdmin)