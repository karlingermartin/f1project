from django.shortcuts import render
from f1app.models import Driver, Constructor, Circuit, Races
from f1app.forms import DriverForm, ConstructorForm, CircuitForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"

#DriverViews
class DriverListView(ListView):
    model = Driver

    def get_queryset(self):
        return Driver.objects.all().order_by("-race_wins")

class DriverDetailView(DetailView):
    model = Driver

class DriverCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/driver_detail.html"
    form_class = DriverForm
    model = Driver

class DriverUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/driver_detail.html"
    form_class = DriverForm
    model = Driver

class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    success_url = reverse_lazy("driver_list")

#ConstructorViews
class ConstructorListView(ListView):
    model = Constructor

    def get_queryset(self):
        return Constructor.objects.all().order_by("-constructor_race_wins")

class ConstructorDetailView(DetailView):
    model = Constructor

class ConstructorCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/constructor_detail.html"
    form_class = ConstructorForm
    model = Constructor

class ConstructorUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/constructor_detail.html"
    form_class = ConstructorForm
    model = Constructor

class ConstructorDeleteView(LoginRequiredMixin, DeleteView):
    model = Constructor
    success_url = reverse_lazy("constructor_list")

#CircuitViews
class CircuitListView(ListView):
    model = Circuit

    def get_queryset(self):
        return Circuit.objects.all() #.order_by("-races")

class CircuitDetailView(DetailView):
    model = Circuit

class CircuitCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/circuit_detail.html"
    form_class = CircuitForm
    model = Circuit

class CircuitUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/circuit_detail.html"
    form_class = CircuitForm
    model = Circuit

class CircuitDeleteView(LoginRequiredMixin, DeleteView):
    model = Circuit
    success_url = reverse_lazy("circuit_list")

#Races
class RacesListView(ListView):
    model = Races

    def get_queryset(self):
        return Races.objects.all()