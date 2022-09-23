from app1.views import *


@login_required
def Prescricao_add(request):
    if request.method == 'POST':
        form = PrescricaoForm(request.POST)
        if form.is_valid():
            novo_prescricao = form.save(commit=False)
            novo_prescricao.save()
            return HttpResponseRedirect('/prescricao_list')
    else:
        form = PrescricaoForm()

    prescricao = Prescricao.objects.all()

    return render(request, 'prescricao_form.html', {'form': form,
    'prescricao': prescricao})