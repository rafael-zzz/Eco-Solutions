from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ONG, Residuos
from django.http import HttpResponseForbidden
from .forms import ONGForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')

                # pega a ONG do usuário e redireciona para a página específica dela
                try:
                    ong = user.ong
                    return redirect('ong_detail', id=ong.id) 
                except ONG.DoesNotExist:
                    # caso o usuário não tenha uma ONG associada, redireciona para 'mapa'
                    return redirect('mapa')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está em uso.')
            return render(request, 'cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        auth_login(request, user)
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('home')

    return render(request, 'cadastro.html')


def mapa(request):
    locais = ONG.objects.all()
    return render(request, 'mapa.html', {'locais': locais})
 
def verificar_ong(request, id):
    ong = get_object_or_404(ONG, id=id, usuario=request.user)
    residuos = Residuos.objects.filter(ong=ong)
    return render(request, 'ong_detail.html', {'ong': ong, 'residuos': residuos})

def update_ong(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)
    
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
    residuos = Residuos
    print(residuos)
    return render(request, 'ong_detail.html', {'ong': ong, 'residuos': residuos})

def adicionar_residuo(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        quantidade = request.POST.get('quantidade')
        peso = request.POST.get('peso')
        status = request.POST.get('status')
        descricao = request.POST.get('descricao')

        Residuos.objects.create(
            ong=ong,
            tipo=tipo,
            quantidade=quantidade,
            peso=peso,
            status=status,
            descricao=descricao,
        )
        return redirect('ong_detail', id=ong_id) 
    return redirect('home')


def remover_residuo(request, residuo_id):
    resíduo = get_object_or_404(Residuos, id=residuo_id)
    resíduo.delete()
    return redirect('ong_detail', id=resíduo.ong.id)  
