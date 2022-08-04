from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home_DF.html')


def evolucaocomopatologia(request):
    return render(request, 'a_evolucao_como_uma_patologia.html')


def nulidadedaexistencia(request):
    return render(request, 'sobre_a_nulidade_da_existencia.html')
