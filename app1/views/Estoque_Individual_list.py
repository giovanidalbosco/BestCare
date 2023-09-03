from app1.views import *


@login_required
def Estoque_Individual_list(request):
    search = request.GET.get('search')
    residentes = Pessoas.objects.filter(pessoa_classe=2)
    
    if search:
        estoque_individual = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome__icontains=search)
        residente = Pessoas.objects.get(pessoa_nome=search)
    else:
        estoque_individual = ''
        residente = ''

    context = {
        'estoque_individual': estoque_individual,
        'residentes': residentes,
        'dono': residente 
    }

    return render(request, template_name='estoque_individual_list.html', context=context)