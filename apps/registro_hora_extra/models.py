from django.db import models

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=200, help_text='Motivo')
    def __str__(self):
        return self.motivo
