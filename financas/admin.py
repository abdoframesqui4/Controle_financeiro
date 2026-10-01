from django.contrib import admin

from .models import Categoria, Conta, Despesa, MetaEconomia, Receita

# Registra as 5 tabelas no painel administrativo (/admin)
admin.site.register(Categoria)
admin.site.register(Conta)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(MetaEconomia)
