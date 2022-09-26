from app1.views import *


@login_required
def Estoque_Individual_list(request):
    search = request.GET.get('search')
    pessoa_nome = Pessoas.objects.all()
    if search:
        dono_estoque = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome__icontains=search)
    else:
        dono_estoque = ''

    context = {
        'estoque_individual': dono_estoque,
        'pessoa_nome': pessoa_nome,
    }

    return render(request, template_name='estoque_individual_list.html', context=context)