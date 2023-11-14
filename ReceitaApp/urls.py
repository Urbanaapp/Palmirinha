from django.urls import path
from ReceitaApp import views

# path('',           views.index,          name='index'),
#      'caminho',    nome da  view(def),   nome url
urlpatterns = [
    path('', views.index, name='index'), 
    path('receitas/', views.receitas, name='receitas'),  
    path('receita/<int:id>', views.detalhes_receitas, name='receita')
]