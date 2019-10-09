from django.urls import path
from .views import ListarFuncionarios
urlpatterns = [
    path('listar',ListarFuncionarios.as_view(), name="Listar_Funcionarios"),
]
