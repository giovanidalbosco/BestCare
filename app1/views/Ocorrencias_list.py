from app1.views import *


@login_required
def Ocorrencias_list(request):
    search = request.GET.get('search')
    if search:
        ocorrencia = Ocorrencias.objects.filter(pessoa_classe__icontains=('2','1'))
    else:
        ocorrencia = Ocorrencias.objects.all()

    return render(request, 'ocorrencias_list.html', {'ocorrencia': ocorrencia})
