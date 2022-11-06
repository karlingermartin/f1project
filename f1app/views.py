from django.shortcuts import render
from django.http import HttpRequest
from f1app.models import Driver, Constructor, Circuit, Races, Result, Analysis
from f1app.forms import DriverForm, ConstructorForm, CircuitForm, RacesForm, ResultForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from f1app.analysis import ChartGenerator

# Create your views here.


class AboutView(TemplateView):
    template_name = "index.html"


# DriverViews
class DriverListView(ListView):
    model = Driver

    def get_queryset(self):
        return Driver.objects.all()


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


# ConstructorViews
class ConstructorListView(ListView):
    model = Constructor

    def get_queryset(self):
        return Constructor.objects.all()


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


# CircuitViews
class CircuitListView(ListView):
    model = Circuit

    def get_queryset(self):
        return Circuit.objects.all()


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


# Races
class RacesListView(ListView):
    model = Races

    def get_queryset(self):
        return Races.objects.all().order_by("-date")


class RacesDetailView(DetailView):
    model = Races

    def get_context_data(self, **kwargs):
        race = kwargs["object"]
        race_details = {

            "name": race.race_name,
            "year": race.race_year,
            "results": race.results.all()

        }
        print(kwargs)
        return race_details


class RacesCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/races_detail.html"
    form_class = RacesForm
    model = Races


class RacesUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/races_detail.html"
    form_class = RacesForm
    model = Races


class RacesDeleteView(LoginRequiredMixin, DeleteView):
    model = Races
    success_url = reverse_lazy("races_list")


# Results
class ResultListView(ListView):
    model = Result

    def get_queryset(self):
        return Result.objects.all()


class ResultDetailView(DetailView):
    model = Result


class ResultCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/races_detail.html"
    form_class = ResultForm
    model = Result


class ResultUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/races_detail.html"
    form_class = ResultForm
    model = Result


class ResultDeleteView(LoginRequiredMixin, DeleteView):
    model = Result
    success_url = reverse_lazy("races_list")


# Analysis
class AnalysisListView(ListView):
    model = Analysis

    def get_context_data(self, **kwargs):
        c = ChartGenerator()

        context = {}
        context['chart'] = c.first_ten()
        return context
