from app1.views import *


@login_required
def Uso_Consumo_edit(request, id):
    uso_consumo = get_object_or_404(Uso_Consumo, pk=id)
    form = Uso_ConsumoForm(instance=uso_consumo)
    if (request.method == 'POST'):
        form = Uso_ConsumoForm(request.POST, instance=uso_consumo)
        if (form.is_valid()):
            uso_consumo.save()
            return redirect('/uso_consumo_list')
        else:
            return render(request, 'uso_consumo_form.html', {
                'form': form, 
                'uso_consumo': uso_consumo
            })
    else:
        return render(request, 'uso_consumo_form.html', {
            'form': form,
            'uso_consumo': uso_consumo
        })