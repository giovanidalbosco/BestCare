from app1.views import *

def index(request):
    return render(request, 'index.html')