from django.shortcuts import render
from .models import Caso  

def lista_casos(request):
   
    todos_los_casos = Caso.objects.all()
    

    return render(request, 'expedientes/lista.html', {'casos': todos_los_casos})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CasoForm


def borrar_caso(request, id):
    caso = get_object_or_404(Caso, id=id)
    caso.delete()
    return redirect('lista') # Nos regresa a la página principal


def editar_caso(request, id):
    caso = get_object_or_404(Caso, id=id)
    if request.method == 'POST':
        form = CasoForm(request.POST, instance=caso)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = CasoForm(instance=caso)
    return render(request, 'expedientes/editar.html', {'form': form, 'caso': caso})
