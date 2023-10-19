from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Reserva, Stand
from .forms import ReservaForm, StandForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
# Create your views here.


class IndexHomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_reserva"] = Reserva.objects.count()
        context["total_stands"] = Stand.objects.count()
        return context
    
class IndexLog(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_reserva"] = Reserva.objects.count()
        context["total_stands"] = Stand.objects.count()
        return context    
    
class ReservaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "form_reserva.html"
    success_message = "Reserva cadastrada com sucesso!"
    error_message = "Erro ao cadastrar reserva!"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi cadastrada com sucesso")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

class ReservasListView(LoginRequiredMixin, generic.ListView):
    model = Reserva
    template_name = "lista_reserva.html"
    paginate_by = 3

class ReservaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("lista_reservas")
    success_message = "Reserva excluído com sucesso!"



class ReservaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "form_reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Sua reserva foi atualizada com sucesso")
        return super().form_valid(form)


class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "detalhe_reserva.html"  

class StandCreateView(LoginRequiredMixin, generic.CreateView):
        model = Stand
        form_class = StandForm
        success_url = reverse_lazy("lista_stands")
        template_name = "form_stand.html"

        def form_valid(self, form):
            messages.success(self.request, "Seu stand foi cadastrado com sucesso")
            return super().form_valid(form)

class StandListView(LoginRequiredMixin, generic.ListView):
    model = Stand
    template_name = "lista_stand.html"
    paginate_by = 3

class StandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("lista_stands")
    template_name = "form_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Seu stand foi atualizado com sucesso")
        return super().form_valid(form)

class StandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("lista_stands")
    success_message = "Stand excluído com sucesso!"

class StandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stand
    template_name = "detalhe_stand.html" 