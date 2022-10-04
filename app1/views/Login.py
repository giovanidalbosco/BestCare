from app1.views import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def Login(request):
    loginForm = LoginForm()
    mensagem = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        nomeUsuario = request.POST['usuario']
        senha = request.POST['senha']
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            usuario = authenticate(username=nomeUsuario, password=senha)
            if usuario is not None:
                login(request, usuario)
                return redirect('/agenda')
            else:
                mensagem = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }

    context = {
        'form': loginForm,
        'mensagem': mensagem,
        'titulo': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Cadastre-se',
        'link_href': '/cadastro'
    }

    return render(request, template_name='login.html', context=context, status=200)