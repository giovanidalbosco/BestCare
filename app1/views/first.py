from app1.views import *


def first(request):
    return render(request, 'first.html')