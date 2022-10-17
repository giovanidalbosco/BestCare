from app1.views import *


@login_required
def Residentes_edit(request, id):
    residente = get_object_or_404(Pessoas, pk=id)
    form = ResidentesForm(instance=residente)
    if (request.method == 'POST'):
        form = ResidentesForm(request.POST, instance=residente)
        if (form.is_valid()):
            residente = form.save(commit=False)
            residente.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return redirect('/residentes_list')
        else:
            return render(request, 'residentes_form.html', {
                'form': form, 
                 'residente': residente
             })
    else:
        return render(request, 'residentes_form.html', {
            'form': form,
            'residente': residente
        })

