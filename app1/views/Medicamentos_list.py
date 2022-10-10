from app1.views import *


@login_required
def Medicamentos_list(request):
    search = request.GET.get('search')
    if search:
        medicamentos = Medicamentos.objects.filter(medicamento_nome__icontains=search)
    else:
        medicamentos = Medicamentos.objects.all()

    return render(request, 'medicamentos_list.html', {'medicamentos': medicamentos})