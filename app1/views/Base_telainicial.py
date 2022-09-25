from app1.views import *


@login_required
def Base_telainicial(request):
    return render(request, 'base_telainicial.html')