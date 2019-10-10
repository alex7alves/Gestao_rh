from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView , DeleteView
from .models import Funcionario

class ListarFuncionarios(ListView):
    model = Funcionario

    # Sobrescrevendo esse metodo para pegar somente
    # os funcionarios da mesma empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class EditarFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']


class DeletarFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("Listar_Funcionarios")
