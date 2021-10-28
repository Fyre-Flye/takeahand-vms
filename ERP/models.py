from django.db import models

# Create your models here.

class Voluntarios(models.Model):
    nome = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)
    numero_de_id = models.IntegerField()
