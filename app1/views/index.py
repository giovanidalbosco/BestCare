from app1.views import *


@login_required
def index(request):
    return render(request, 'index.html')