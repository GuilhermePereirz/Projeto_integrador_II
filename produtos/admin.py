from django.contrib import admin
from .models import Produto, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'status']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
