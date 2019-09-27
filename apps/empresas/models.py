from django.db import models


class empresa(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome da empresa')
    def __str__(self):
        return self.nome
