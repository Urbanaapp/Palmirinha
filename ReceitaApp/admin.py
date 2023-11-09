from django.contrib import admin

from ReceitaApp.models import Categoria 
from ReceitaApp.models import Receita

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Receita)