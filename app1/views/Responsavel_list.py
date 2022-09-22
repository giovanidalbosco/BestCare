from app1.views import *


@login_required
def Residentes_list(request):
    search = request.GET.get('search')
    if search:
        responsavel = Pessoas.objects.filter(pessoa_nome__icontains=search)
    else:
        responsavel = Pessoas.objects.all()

    context = {
        'responsavel_nome': responsavel
    }

    return render(request, 'responsavel_list.html', {'responsavel': responsavel})