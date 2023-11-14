from django.db import models

# Create your models here.

OPCOES = [
        ('F','Facil'),
        ('M','Moderado'),
        ('D','Dificil')        
        ]

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome +''
    
class Receita(models.Model):

       
    nome =models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=2000)
    mododepreparo = models.TextField(max_length=8000)
    graudedificuldade = models.CharField(max_length=10, choices=OPCOES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(null = True,upload_to='imagens/', blank= True)

    def __str__(self):
        return self.nome +''
    
