from django import forms
from . models import *


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = "__all__"


class AvaliacaoForm2(forms.ModelForm):
    class Meta:
        model = Avaliacao2
        fields = "__all__"
