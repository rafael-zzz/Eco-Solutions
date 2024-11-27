from django import forms
from .models import ONG, Residuos


class ONGForm(forms.ModelForm):
    class Meta:
        model = ONG
        fields = ['nome', 'cnpj', 'endereco','latitude','longitude','informacao','imagem']  
latitude = forms.CharField(max_length=255, required=True)
longitude = forms.CharField(max_length=255, required=True)

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuos
        fields = ['tipo', 'quantidade', 'peso', 'status', 'descricao']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control rounded-md bg-white/20 border-transparent focus:border-purple-500 focus:bg-white/30 focus:ring-0 text-white'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control rounded-md bg-white/20 border-transparent focus:border-purple-500 focus:bg-white/30 focus:ring-0 text-white'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control rounded-md bg-white/20 border-transparent focus:border-purple-500 focus:bg-white/30 focus:ring-0 text-white'}),
            'status': forms.Select(attrs={'class': 'form-control rounded-md bg-white/20 border-transparent focus:border-purple-500 focus:bg-white/30 focus:ring-0 text-white'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control rounded-md bg-white/20 border-transparent focus:border-purple-500 focus:bg-white/30 focus:ring-0 text-white', 'rows': 3}),
        }
