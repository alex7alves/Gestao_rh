from django.urls import path
from .views import ListarFuncionarios, EditarFuncionario, DeletarFuncionario
urlpatterns = [
    path('listar',ListarFuncionarios.as_view(), name="Listar_Funcionarios"),
    path('editar/<int:pk>',EditarFuncionario.as_view(), name="Editar_Funcionario"),
    path('deletar/<int:pk>',DeletarFuncionario.as_view(), name="Deletar_Funcionario"),
]
