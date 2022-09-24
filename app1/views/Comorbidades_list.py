from app1.views import *


@login_required
def Comorbidades_list(request):
    search = request.GET.get('search')
    if search:
        comorbidade = Comorbidades.objects.filter(comorbidade_nome__icontains=search)
    else:
        comorbidade = Comorbidades.objects.all()

    return render(request, 'comorbidades_list.html',
                  {'comorbidade': comorbidade})