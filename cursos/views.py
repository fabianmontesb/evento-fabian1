from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Inscripcion
from django.contrib.auth.decorators import login_required


login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creador = request.user
            evento.save()
            return redirect('eventos:detalle_evento', evento_id=evento.id)
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

login_required
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    inscritos = Inscripcion.objects.filter(evento=evento)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'inscritos': inscritos})

login_required
def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    Inscripcion.objects.create(evento=evento, usuario=request.user)
    return redirect('eventos:detalle_evento', evento_id=evento.id)
from django.shortcuts import render

# Create your views here.
