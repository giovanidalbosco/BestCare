from app1.views import *


@login_required
def Estoque_Individual_list(request, id=0):
    search = request.GET.get('search')
    pessoa_nome = Pessoas.objects.all()
    print(f'pessoas:{pessoa_nome}')
    if search:

        pessoa_selec = Pessoas.objects.filter(pessoa_nome__icontains=search).first()
        dono_estoque = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome__icontains=pessoa_selec)
        print(dono_estoque)
        
        # item = dono_estoque.get('')
        print(pessoa_nome)

    elif id!=0:
        pessoa_selec = Pessoas.objects.filter(pessoa_pk=id).first()
        dono_estoque = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome__icontains=pessoa_selec) 
        print(dono_estoque)
        

    else:
        dono_estoque = ''
        pessoa_selec = ''

    context = {
        'estoque_individual': dono_estoque,
        'pessoa_nome': pessoa_nome,
        'pessoa_selec': pessoa_selec,
    }

    return render(request, template_name='estoque_individual_list.html', context=context)