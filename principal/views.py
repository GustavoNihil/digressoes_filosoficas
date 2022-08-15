from django.shortcuts import render

# Create your views here.
from . models import *
from . forms import *


def index(request):
    return render(request, 'home_DF.html')


def evolucaocomopatologia(request):
    mensagem = None
    total_de_avaliacoes = len(Avaliacao.objetos.all())
    soma = 0
    for u in Avaliacao.objetos.all():
        soma += u.avaliação
    try:
        media = round(soma / total_de_avaliacoes, 2)
    except:
        media = 0
    if request.method == "GET":  # Se a requisição for um método Get ele executa as linhas abaixo
        form = AvaliacaoForm()
        context = {
            'form': form,
            'total_de_avaliacoes': total_de_avaliacoes,
            'media': media
        }
        return render(request, 'a_evolucao_como_uma_patologia.html', context=context)
    else:
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            dados = request.POST
            variavel_email = dados.get("email")
            try:
                email2 = Avaliacao.objetos.filter(email=variavel_email).first()
                email2 = email2.email
            except:
                email2 = None
            if variavel_email == email2:
                mensagem = "Este email já foi inserido"
                context = {
                    'form': form,
                    'mensagem': mensagem,
                    'total_de_avaliacoes': total_de_avaliacoes,
                    'media': media
                }
            # fazer verificação se o email já foi cadastrado
            else:
                avaliacao = form.save()
                form = AvaliacaoForm()
                total_de_avaliacoes = len(Avaliacao.objetos.all())
                soma = 0
                for linha in Avaliacao.objetos.all():
                    soma += linha.avaliação
                try:
                    media = round(soma / total_de_avaliacoes,
                                  2)  # "round" faz o arredondamento, e o segundo parâmetro defino quantos números serão exibidos após a vírgula
                except:
                    media = 0
                mensagem = "Avaliação enviada com sucesso"
                context = {
                    'form': form,
                    'mensagem': mensagem,
                    'total_de_avaliacoes': total_de_avaliacoes,
                    'media': media
                }
        if mensagem == None:
            context = {
                'form': form,
                'total_de_avaliacoes': total_de_avaliacoes,
                'media': media
            }
        return render(request, 'a_evolucao_como_uma_patologia.html', context=context)


def nulidadedaexistencia(request):
    mensagem = None
    total_de_avaliacoes = len(Avaliacao2.objetos.all())
    soma = 0
    for u in Avaliacao2.objetos.all():
        soma += u.avaliação
    try:
        media = round(soma / total_de_avaliacoes, 2)
    except:
        media = 0
    if request.method == "GET":  # Se a requisição for um método Get ele executa as linhas abaixo
        form = AvaliacaoForm2()
        context = {
            'form': form,
            'total_de_avaliacoes': total_de_avaliacoes,
            'media': media
        }
        return render(request, 'sobre_a_nulidade_da_existencia.html', context=context)
    else:
        form = AvaliacaoForm2(request.POST)
        if form.is_valid():
            dados = request.POST
            variavel_email = dados.get("email")
            try:
                email2 = Avaliacao2.objetos.filter(email=variavel_email).first()
                email2 = email2.email
            except:
                email2 = None
            if variavel_email == email2:
                mensagem = "Este email já foi inserido"
                context = {
                    'form': form,
                    'mensagem': mensagem,
                    'total_de_avaliacoes': total_de_avaliacoes,
                    'media': media
                }
            # fazer verificação se o email já foi cadastrado
            else:
                avaliacao = form.save()
                form = AvaliacaoForm2()
                total_de_avaliacoes = len(Avaliacao2.objetos.all())
                soma = 0
                for linha in Avaliacao2.objetos.all():
                    soma += linha.avaliação
                try:
                    media = round(soma / total_de_avaliacoes, 2)  # "round" faz o arredondamento, e o segundo parâmetro defino quantos números serão exibidos após a vírgula
                except:
                    media = 0
                    mensagem = "Avaliação enviada com sucesso"
                    context = {
                    'form': form,
                    'mensagem': mensagem,
                    'total_de_avaliacoes': total_de_avaliacoes,
                    'media': media
                }
        if mensagem == None:
            context = {
                'form': form,
                'total_de_avaliacoes': total_de_avaliacoes,
                'media': media
            }
        return render(request, 'sobre_a_nulidade_da_existencia.html', context=context)

