from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Stand
from .forms import ReservaForm, StandForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
# Create your views here.


class IndexHomeView(generic.TemplateView):
    template_name = "index.html"

    
    
class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "form_reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi cadastrada com sucesso")
        return super().form_valid(form)

class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "lista_reserva.html"
    paginate_by = 2

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("lista_reservas")

    def form_valid(self, form):
        messages.error(self.request, "Sua reserva foi cancelada")
        return super().form_valid(form)

class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "form_reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi atualizada com sucesso")
        return super().form_valid(form)


class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "detalhe_reserva.html"  

class StandCreateView(generic.CreateView):
        model = Stand
        form_class = StandForm
        success_url = reverse_lazy("lista_stands")
        template_name = "form_stand.html"

        def form_valid(self, form):
            messages.success(self.request, "Seu stand foi cadastrado com sucesso")
            return super().form_valid(form)

class StandListView(generic.ListView):
    model = Stand
    template_name = "lista_stand.html"
    paginate_by = 2

class StandUpdateView(generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Seu stand foi atualizado com sucesso")
        return super().form_valid(form)

class StandDeleteView(generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("lista_stands")
    
    def form_valid(self, form):
        messages.error(self.request, "Seu stand foi removido")
        return super().form_valid(form)

class StandDetailView(generic.DetailView):
    model = Stand
    template_name = "detalhe_stand.html" 