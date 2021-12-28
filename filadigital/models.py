from django.db import models


# Create your models here.

class Fila(models.Model):
    empresa = models.CharField(max_length=200)
    nome_fila = models.CharField(max_length=200)
    vaga = models.CharField(max_length=200);
    site = models.CharField(max_length=200);
    status = models.CharField(max_length=200);
    
    def __str__(self):
        return self.empresa
    
    