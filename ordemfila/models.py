from django.db import models
from django.db.models.deletion import CASCADE
from filadigital.models import Fila
from fila.models import vaga_fila

# Create your models here.

class ordem_fila(models.Model):
    fila = models.CharField(max_length=200)
    nome_usuario = models.CharField(max_length=200)
    celular_usuario = models.CharField(max_length=200)
    posicao = models.IntegerField(blank=True, null=True)
    posicao2 = models.IntegerField(blank=True, null=True)
    posicao3 = models.IntegerField(blank=True, null=True)
    vaga = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome_usuario
    
