from app1.views import *


def Cad(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
    else:
        form = Cadastro()

    return render(request, 'cadastro.html', {'form': form})