from app1.views import *


@login_required
def Residentes_list(request):
    search = request.GET.get('search')
    if search:
        residente = Pessoas.objects.filter(pessoa_classe__icontains='2')
    else:
        residente = Pessoas.objects.filter(pessoa_classe__icontains='2')

    return render(request, 'residentes_list.html', {'residente': residente})