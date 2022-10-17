from datetime import datetime, timedelta, date  
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from requests import RequestException, request

from app1.models import Event, Pessoas
from app1.utils import Calendar
from app1.forms import EventForm
from app1.views import *

class Agenda(generic.ListView):
    model = Event
    template_name = 'agenda.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)


        residentes = Pessoas.objects.filter(pessoa_classe='2')

        search = self.request.GET.get('search')
        if search:
            residente = Pessoas.objects.get(pessoa_nome=search)
            html_cal = cal.formatmonth(residente.id, withyear=True)
            context['dono'] = residente
        else:
            html_cal = cal.formatmonth(withyear=True)


        context['residentes'] = residentes
        # Call the formatmonth method, which returns our calendar as a table
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, residente_id=None, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    
    residente = get_object_or_404(Pessoas, id=residente_id)
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        evento = form.save(commit=False)
        if residente_id:
            evento.event_pessoa_nome = residente
        evento.save()
        if hasattr(form, 'save_m2m'):
            form.save_m2m()
        return HttpResponseRedirect(f'/agenda/?search={residente.pessoa_nome}')
    return render(request, 'event.html', {'form': form, 'residente': residente})

def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect(f'/agenda/?search={event.event_pessoa_nome.pessoa_nome}')