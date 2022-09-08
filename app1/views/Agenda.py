from app1.views import *


@login_required
def Agenda(request):
    return render(request, 'agenda.html')