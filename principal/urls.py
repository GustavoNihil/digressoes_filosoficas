from django.urls import path
from . import views

# app_name = 'principal'
# referenciação, assim como o name do path (ex: 'principal:nulidadedaexistencia')


urlpatterns = [
    path('', views.index, name='home'),
    path('evolucaocomopatologia/', views.evolucaocomopatologia, name='evolucaocomopatologia'),
    path('nulidadedaexistencia/', views.nulidadedaexistencia, name='nulidadedaexistencia'),
]