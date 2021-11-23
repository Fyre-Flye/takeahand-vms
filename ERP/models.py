from django.db import models

# Create your models here.

class Voluntarios(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30) # t
    cpf = models.CharField(max_length=30) # t 
    funcao = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30) # t 
    telefone = models.CharField(max_length=30) # t
    horas_semanais = models.CharField(max_length=30)
    horas_contribuidas = models.CharField(max_length=30)

    

