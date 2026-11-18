from django.contrib import admin
from .models import Categoria, projeto

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ["nome", "ano", "categoria"]

admin.site.register(Categoria)
admin.site.register(projeto, ProjetoAdmin)