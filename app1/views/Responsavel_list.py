from app1.views import *


@login_required
def Responsavel_list(request):
    search = request.GET.get('search')
    if search:
        responsavel = Pessoas.objects.filter(pessoa_nome__icontains='3')
    else:
        responsavel = Pessoas.objects.filter(pessoa_classe__icontains='3')


    return render(request, 'responsavel_list.html', {'responsavel': responsavel})
