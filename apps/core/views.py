from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Obrigar se logar para acessar -> vai para pagina de login
@login_required
def home(request):
    return render(request,'core/index.html')
