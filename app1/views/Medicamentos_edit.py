from app1.views import *


@login_required
def Medicamentos_edit(request, id):
    medicamentos = get_object_or_404(Medicamentos, pk=id)
    form = MedicamentosForm(instance=medicamentos)
    if (request.method == 'POST'):
        form = MedicamentosForm(request.POST, instance=medicamentos)
        if (form.is_valid()):
            medicamentos.save()
            return redirect('/medicamentos_list')
        
        else:
            return render(request, 'medicamentos_form.html', {
                'form': form, 
                'medicamentos': medicamentos
            })
    else:
        return render(request, 'medicamentos_form.html', {
            'form': form,
            'medicamentos': medicamentos
        })