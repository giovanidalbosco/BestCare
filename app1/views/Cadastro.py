from app1.views import *
from django.contrib.auth.models import User


def Cadastro(request):
    cadastroForm = CadastroForm()
    mensagem = None
    if request.user.is_authenticated:
        return redirect('/agenda')
    
    if request.method == 'POST':
        nomeUsuario = request.POST['usuario']
        nomeCompleto = request.POST['nomeCompleto']
        entidade = request.POST['entidade']
        email = request.POST['email']
        senha = request.POST['senha']
        cadastroForm = CadastroForm(request.POST)
        
        if cadastroForm.is_valid():
            # Aqui verificamos se existe usuário ou e-mail com esse cadastro
            verificaNomeUsuario = User.objects.filter(username=nomeUsuario).first()
            verificaEmail = User.objects.filter(email=email).first()
    
            if verificaNomeUsuario is not None:
                mensagem = { 'type': 'danger', 'text': 'Já existe um usuário com este nome!' }
            elif verificaEmail is not None:
                mensagem = { 'type': 'danger', 'text': 'Já existe um usuário com este e-mail!' }
            else:
                # novo_cuidador = Pessoas()
                # novo_cuidador.cria_cuidador(nomeUsuario, email)
                # novo_cuidador.save()
                usuario = User.objects.create_user(nomeUsuario, email, senha)
                usuario.first_name = nomeCompleto
                usuario.last_name = entidade
                usuario.save()
                if usuario is not None:
                    mensagem = { 'type': 'success', 'text': 'Conta criada com sucesso!' }
                else:
                    mensagem = { 'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.' }
    
    context = {
        'form': cadastroForm,
        'mensagem': mensagem,
        'titulo': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Entrar',
        'link_href': '/login'
    }
    return render(request, template_name='login.html', context=context, status=200)
