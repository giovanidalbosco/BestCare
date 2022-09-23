from app1.views import *


@login_required
def Prescricao_list(request):
    search = request.GET.get('search')
    if search:
        prescricao = Prescricao.objects.filter(prescricao_pessoa_nome__icontains=search)
    else:
        prescricao = Prescricao.objects.all()

    return render(request, 'prescricao_list.html', {'prescricao': prescricao})