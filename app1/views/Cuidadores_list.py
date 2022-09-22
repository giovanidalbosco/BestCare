from app1.views import *


@login_required
def Cuidadores_list(request):
    search = request.GET.get('search')
    if search:
        cuidador = Pessoas.objects.filter(pessoa_classe__icontains='1')
    else:
        cuidador = Pessoas.objects.filter(pessoa_classe__icontains='1')

    return render(request, 'cuidadores_list.html',
                  {'cuidador': cuidador})