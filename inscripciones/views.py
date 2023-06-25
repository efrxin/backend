from django.shortcuts import render, get_object_or_404, redirect
from .forms import InscripcionForm
from .models import Inscripcion

def inscripciones_list(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripciones/inscripciones_list.html', {'inscripciones': inscripciones})

def inscripcion_agregar(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripciones:inscripciones_list')
    else:
        form = InscripcionForm()
    return render(request, 'inscripciones/inscripcion_agregar.html', {'form': form})

def inscripcion_editar(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('inscripciones:inscripciones_list')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'inscripciones/inscripcion_editar.html', {'form': form, 'inscripcion': inscripcion})

def inscripcion_eliminar(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('inscripciones:inscripciones_list')
    return render(request, 'inscripciones/inscripcion_eliminar.html', {'inscripcion': inscripcion})
