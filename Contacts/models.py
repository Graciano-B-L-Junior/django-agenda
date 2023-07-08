from typing import Any
from django.db import models

# Create your models here.

class Contact(models.Model):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    primeiro_nome = models.CharField(max_length=50,verbose_name='Primeiro nome')
    ultimo_nome = models.CharField(max_length=50,verbose_name='Ultimo nome',blank=True)
    email = models.EmailField(unique=True,blank=False,default="teste@teste.com")
    description = models.TextField(blank=True)
    celular = models.CharField(blank=True,max_length=11)
    show = models.BooleanField(default=False)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.primeiro_nome
    
