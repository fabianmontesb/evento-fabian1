from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Evento, Inscripcion
from .forms import RegistroForm, EventoForm

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('lista_eventos')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    form_class = EventoForm
    template_name = 'eventos/nuevo_evento.html'
    success_url = reverse_lazy('lista_eventos')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EventoDetailView(DetailView):
    model = Evento
    template_name = 'eventos/detalle_evento.html'

def inscribir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    Inscripcion.objects.create(evento=evento, usuario=request.user)
    return redirect('detalle_evento', pk=evento_id)




