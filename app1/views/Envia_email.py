from app1.views import *

@login_required
def envia_email(request):                      #Quem envia              #Quem recebe
    send_mail('Assunto', 'Counteúdo', 'bestcareauth@outlook.com', ['quemrecebe@email.com'], fail_silently=False,)
    return render(request, 'email.html')
