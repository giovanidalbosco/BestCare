from app1.views import *


@login_required
def Ocorrencias_list(request):
    search = request.GET.get('search')
    if search:
        ocorrencia = Ocorrencias.objects.filter(ocorrencia_nome__icontains=search)
    else:
        ocorrencia = Ocorrencias.objects.all()

    context = {
        'ocorrencia_nome': ocorrencia
    }

    return render(request, 'ocorrencias_list.html', {'ocorrencia': ocorrencia})