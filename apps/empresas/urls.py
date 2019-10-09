from django.urls import path
from .views import CriarEmpresa, EditarEmpresa
urlpatterns = [
    path('novo',CriarEmpresa.as_view(), name='Criar_Empresa'),
    path('editar/<int:pk>/',EditarEmpresa.as_view(), name='Editar_Empresa'),
]
