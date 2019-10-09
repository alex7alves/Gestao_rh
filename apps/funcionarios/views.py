from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Funcionario

class ListarFuncionarios(ListView):
    model = Funcionario

    # Sobrescrevendo esse metodo para pegar somente
    # os funcionarios da mesma empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)
