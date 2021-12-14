from django.db import models
from django.db.models.deletion import CASCADE
#from .models import Fila
# Create your models here.

class vaga_fila(models.Model):
    vagas = models.CharField(max_length=200)
    
    def __str__(self):
        return self.vagas