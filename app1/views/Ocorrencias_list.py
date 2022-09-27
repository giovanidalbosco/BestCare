from app1.views import *


@login_required
def Ocorrencias_list(request):
    search = request.GET.get('search')
    if search:
        ocorrencia = Ocorrencias.objects.filter(ocorrencia_pessoa_nome__icontains='2')
    else:
        ocorrencia = Ocorrencias.objects.filter(ocorrencia_pessoa_nome__icontains='2')

    return render(request, 'ocorrencias_list.html', {'ocorrencia': ocorrencia})
