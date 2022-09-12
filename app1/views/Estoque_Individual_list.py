from app1.views import *


@login_required
def Estoque_Individual_list(request):
    search = request.GET.get('search')
    if search:
        estoque = Estoque_Individual.objects.filter(estoque_pessoa_nome__icontains=search)
    else:
        estoque = Estoque_Individual.objects.all()

    context = {
        'estoque_individual': estoque
    }

    return render(request, template_name='estoque_individual_list.html', context=context)