from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .form import ReservaForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def criar(request):
    if request.method == "POST":

        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else: 
        form = ReservaForm()

    return render(request, 'form.html', {'form': form})

def listar(request):
    reservas = Reserva.objects.all() 
    context = {'reservas': reservas}
    return render(request, 'lista.html', context)

def remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar')

def detalhar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, 'detalhe.html', context)