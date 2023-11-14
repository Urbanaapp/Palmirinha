from django.shortcuts import render
from ReceitaApp.models import Receita

# Create your views here.
def index(request):
    #Ações da minha view...
    return render(request, 'index.html')

def receitas(request):
    # buscar receitas no banco
    lista_receitas = Receita.objects.all()


    # Dicionario contento as informações que iremos usar nos template
    context = {
        'receitas': lista_receitas,
       
    }

    return render(request,  'receitas.html', context)

def detalhes_receitas(request, id):
    # busca a receita pelo id informado
    receita = Receita.objects.get(id = id)

    context ={
        'receita':receita
    }
    return render(request,'receita.html', context)


