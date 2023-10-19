"""
URL configuration for finecap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', IndexHomeView.as_view(), name='index'),
    path('index_log', IndexLog.as_view(), name='index_log'),
    path('Criar_reservas/', ReservaCreateView.as_view(), name="reserva"),
    path('lista_reservas/', ReservasListView.as_view(), name='lista_reservas'),
    path('remover_reserva/<int:pk>/', ReservaDeleteView.as_view(), name="remover_reserva"),
    path('reserva_detalhe/<int:pk>/', ReservaDetailView.as_view(), name='reserva_detalhe'),
    path('update/<int:pk>/', ReservaUpdateView.as_view(), name="editar"),
    path('lista_stands/', StandListView.as_view(), name='lista_stands'),
    path('criar_stand/', StandCreateView.as_view(), name="criar_stand"),
    path('remover_stand/<int:pk>/', StandDeleteView.as_view(), name="remover_stand"),
    path('update_stand/<int:pk>/', StandUpdateView.as_view(), name="editar_stand"),
    path('stand_detalhe/<int:pk>/', StandDetailView.as_view(), name='stand_detalhe'),
]