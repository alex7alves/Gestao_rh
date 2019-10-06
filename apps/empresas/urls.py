from django.urls import path
from .views import CriarEmpresa
urlpatterns = [
    path('novo',CriarEmpresa.as_view(), name='Criar_Empresa'),
]
