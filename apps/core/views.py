from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario
# Obrigar se logar para acessar -> vai para pagina de login
@login_required
def home(request):

    dados ={}
    dados['usuario'] = request.user
    return render(request,'core/index.html',dados)
