from app1.views import *


@login_required
def Somos(request):
    return render(request, 'quemSomos.html')