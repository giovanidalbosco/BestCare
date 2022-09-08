from app1.views import *


@login_required
def Inicial(request):
    return render(request, 'telainicial.html')