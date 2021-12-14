from django.contrib import admin
from .models import ordem_fila

# Register your models here.

class ordemFilaAdmin (admin.ModelAdmin):
    list_display = ('vaga', 'fila', 'nome_usuario' )
    list_display_link = ('vaga', 'fila', 'nome_usuario')
    search_fields = ('vaga', 'fila', 'nome_usuario')
    
admin.site.register(ordem_fila, ordemFilaAdmin)