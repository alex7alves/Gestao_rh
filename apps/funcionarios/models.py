from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import empresa

class Funcionario(models.Model):
     nome = models.CharField(max_length=200, help_text='Nome do funcionario')
     usuario = models.OneToOneField(User, on_delete=models.PROTECT)
     departamentos = models.ManyToManyField(Departamento)
     empresa = models.ForeignKey(empresa, on_delete=models.PROTECT,null=True, blank=True)

     def get_absolute_url(self):
         return reverse('Listar_Funcionarios')

     def __str__(self):
         return self.nome
