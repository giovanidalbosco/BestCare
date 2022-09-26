from app1.views import *


@login_required
def SinalVital_list(request):
    search = request.GET.get('search')
    if search:
        sinalvital = SinalVital.objects.filter(sinalVital_pessoa_nome__icontains=search)
    else:
        sinalvital = SinalVital.objects.filter()


    return render(request, 'sinalVital_list.html', {'responsavel': sinalvital})