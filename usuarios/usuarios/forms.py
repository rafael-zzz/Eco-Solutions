

from django import forms
from .models import ONG

class ONGForm(forms.ModelForm):
    class Meta:
        model = ONG
        fields = ['nome', 'cnpj', 'endereco','latitude','longitude','informacao','imagem']  
latitude = forms.CharField(max_length=255, required=True)
longitude = forms.CharField(max_length=255, required=True)
