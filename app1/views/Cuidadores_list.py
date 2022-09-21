from app1.views import *


@login_required
def Cuidadores_list(request):
    search = request.GET.get('search')
    if search:
        cuidador = Pessoas.objects.filter(pessoa_classe__icontains='2')
    else:
        cuidador = Pessoas.objects.all()

    return render(request, 'cuidadores_list.html',
                  {'cuidador': cuidador})