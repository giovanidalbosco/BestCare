from app1.views import *


@login_required
def SinalVital_list(request):
    search = request.GET.get('search')
    if search:
        sinalvital = SinalVital.objects.filter(sinalVital_pessoa_nome__pessoa_nome__icontains=search)
    else:
        sinalvital = SinalVital.objects.all()


    return render(request, 'sinalvital_list.html', {'sinalvital': sinalvital})

