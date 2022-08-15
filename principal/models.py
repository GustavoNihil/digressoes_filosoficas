from django.db import models

# Create your models here.

ESTRELAS = (
    (1, '1 Estrela'),
    (2, '2 Estrelas'),
    (3, '3 Estrelas'),
    (4, '4 Estrelas'),
    (5, '5 Estrelas')
)


class Avaliacao(models.Model):
    email = models.EmailField()
    avaliação = models.PositiveIntegerField(choices=ESTRELAS)
    data_criacao = models.DateTimeField(auto_now=True)

    objetos = models.Manager() #utilizado para fazer operações de busca - Por padrão já é criada e recebe o nome "object"


class Avaliacao2(models.Model):
    email = models.EmailField()
    avaliação = models.PositiveIntegerField(choices=ESTRELAS)
    data_criacao = models.DateTimeField(auto_now=True)

    objetos = models.Manager()