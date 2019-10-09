from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import empresa



class CriarEmpresa(CreateView):
    model = empresa
    fields = ['nome']

    def form_valid(self,form):
        objeto = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = objeto
        funcionario.save()
        return HttpResponse("Empresa cadastrada")


class EditarEmpresa(UpdateView):
    model = empresa
    fields = ['nome']
