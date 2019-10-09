from django.urls import path
from .views import ListarFuncionarios, EditarFuncionario
urlpatterns = [
    path('listar',ListarFuncionarios.as_view(), name="Listar_Funcionarios"),
    path('editar/<int:pk>',EditarFuncionario.as_view(), name="Editar_Funcionario"),
]
