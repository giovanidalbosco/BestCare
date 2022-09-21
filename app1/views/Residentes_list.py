from inspect import Attribute
from app1.views import *


@login_required
def Residentes_list(request):
    search = request.GET.get('search')
    if search:
        residente = Pessoas.objects.filter(pessoa_nome__icontains=search)
    else:
        residente = Pessoas.objects.all()

    context = {
        'residente_nome': residente
    }

    return render(request, 'residentes_list.html', {'residente': residente})