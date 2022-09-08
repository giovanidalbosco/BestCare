from app1.views import *


@login_required
def Solucoes(request):
    return render(request, 'solucoes.html')