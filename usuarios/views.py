from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import  ONG, Residuos, AvaliacaoONG, PerfilUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .forms import ONGForm, ResiduoForm
from django.db.models import Avg,Sum

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')
                try:
                    ong = user.ong
                    return redirect('ong_detail', id=ong.id)
                except ONG.DoesNotExist:
                    # Redireciona para a página do mapa se o usuário não estiver associado a uma ONG
                    return redirect('mapa')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html') 


def user_logout(request):
    auth_logout(request)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('home') 


def home(request):
    return render(request, 'home.html') 


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_avaliador = request.POST.get('is_avaliador') == 'on'

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está em uso.')
            return render(request, 'cadastro.html')

        # Criar usuário
        user = User.objects.create_user(username=username, email=email, password=password1)
        
        # Criar perfil do usuário com a opção de avaliador
        PerfilUsuario.objects.create(
            usuario=user,
            is_avaliador=is_avaliador
        )

        auth_login(request, user)
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('home')

    return render(request, 'cadastro.html')


def mapa(request):
    locais = ONG.objects.prefetch_related('avaliacoes', 'residuos').annotate(
    nota_media=Avg('avaliacoes__nota'),
    capacidade_atual=Sum('residuos__peso',distinct=True)
).all()
    
    context = {
        'locais': [{
            'id': local.id,
            'nome': local.nome,
            'latitude': local.latitude,
            'longitude': local.longitude,
            'informacao': local.informacao,
            'endereco': local.endereco,
            'imagem': local.imagem,
            'whatsapp': local.whatsapp,
            'telefone': local.telefone,
            'horario_funcionamento': local.horario_funcionamento,
            'nota_media': float(local.nota_media) if local.nota_media else 0,
            'capacidade_atual': local.capacidade_atual if local.capacidade_atual else 0,
            'capacidade_maxima': local.capacidade_maxima,
            'capacidade_percentual': (local.capacidade_atual / local.capacidade_maxima) * 100 if local.capacidade_atual and local.capacidade_maxima else 0
            
            
        } for local in locais]
    }
    return render(request, 'mapa.html', context)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

class OngDetailView(LoginRequiredMixin, DetailView):
    model = ONG
    template_name = 'ong_detail.html'
    context_object_name = 'ong'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        # Filtra para que apenas a ONG do usuário logado seja acessada
        return ONG.objects.filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['residuos'] = Residuos.objects.filter(ong=self.object)
        return context

    
from .forms import ONGForm

def update_ong(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)
    
    # Verifica se o usuário logado é o dono da ONG
    if ong.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar esta ONG.")
    
    if request.method == 'POST':
        form = ONGForm(request.POST, instance=ong)
        if form.is_valid():
            form.save()
            messages.success(request, "Informações atualizadas com sucesso!")
            return redirect('ong_detail', id=ong.id)
    else:
        form = ONGForm(instance=ong)
    
    return render(request, 'ong_detail.html', {'form': form, 'ong': ong})

def ong_detail(request, id):
    ong = get_object_or_404(ONG, id=id)
    residuos = Residuos.objects.filter(ong=ong)  # Certifique-se de filtrar os resíduos pela ONG correta
    return render(request, 'ong_detail.html', {'ong': ong, 'residuos': residuos})

def adicionar_residuo(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)
    
    # Verifica se o usuário é dono da ONG
    if request.user != ong.usuario:
        messages.error(request, 'Você não tem permissão para adicionar resíduos a esta ONG.')
        return redirect('ong_detail', id=ong_id)

    if request.method == 'POST':
        form = ResiduoForm(request.POST)
        if form.is_valid():
            residuo = form.save(commit=False)
            residuo.ong = ong
            residuo.save()
            messages.success(request, 'Resíduo adicionado com sucesso!')
            return redirect('ong_detail', id=ong_id)
    else:
        form = ResiduoForm()

    return redirect('ong_detail', id=ong_id)


def remover_residuo(request, residuo_id):
    resíduo = get_object_or_404(Residuos, id=residuo_id)
    resíduo.delete()
    messages.success(request, 'Resíduo removido com sucesso!')
    return redirect('ong_detail', id=resíduo.ong.id) 


@login_required
def avaliar_ong(request, ong_id):
    if not request.user.perfil.is_avaliador:
        messages.error(request, 'Apenas avaliadores podem avaliar ONGs.')
        return redirect('mapa')

    ong = get_object_or_404(ONG, id=ong_id)
    
    if request.user == ong.usuario:
        messages.error(request, 'Você não pode avaliar sua própria ONG.')
        return redirect('mapa')

    if request.method == 'POST':
        try:
            nota = int(request.POST.get('nota'))
            if not (1 <= nota <= 5):
                raise ValueError('Nota inválida')
            avaliacao, created = AvaliacaoONG.objects.update_or_create(
                ong=ong,
                usuario=request.user,
                defaults={
                    'nota': nota,
                }
            )

            messages.success(request, 
                'Avaliação registrada com sucesso!' if created else 'Avaliação atualizada com sucesso!')
            
        except (ValueError, TypeError):
            messages.error(request, 'Por favor, forneça uma nota válida entre 1 e 5.')
        
    return redirect('mapa')


