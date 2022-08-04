from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('evolucaocomopatologia/', views.evolucaocomopatologia, name='evolucaocomopatologia'),
    path('nulidadedaexistencia/', views.nulidadedaexistencia, name='nulidadedaexistencia'),
]