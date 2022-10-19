
from django.shortcuts import render
from django.http import HttpRequest
from f1app.models import Driver, Constructor, Circuit, Races, Result, Analysis
from f1app.forms import DriverForm, ConstructorForm, CircuitForm, RacesForm, ResultForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import io, base64
#from django.db.models.functions import TruncDay
#from matplotlib.ticker import LinearLocator
import numpy as np

# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"


#DriverViews
class DriverListView(ListView):
    #paginate_by = 50
    model = Driver

    def get_queryset(self):
        return Driver.objects.all()#.order_by("-race_wins")

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
        return Constructor.objects.all()#.order_by("-constructor_race_wins")

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


#Races
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
        #race_details['results'] = race.results.all()
        print(kwargs)
        return race_details 

class RacesCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/race_detail.html"
    form_class = RacesForm
    model = Races

class RacesUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/race_detail.html"
    form_class = RacesForm
    model = Races

class RacesDeleteView(LoginRequiredMixin, DeleteView):
    model = Races
    success_url = reverse_lazy("race_list")


#Results
class ResultListView(ListView):
    model = Result

    def get_queryset(self):
        return Result.objects.all()

class ResultDetailView(DetailView):
    model = Result

class ResultCreateView(LoginRequiredMixin, CreateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/result_detail.html"
    form_class = ResultForm
    model = Result

class ResultUpdateView(LoginRequiredMixin, UpdateView):
    login_url: "registration/login.html"
    redirect_field_name: "f1app/races_detail.html"
    form_class = ResultForm
    model = Result

class ResultDeleteView(LoginRequiredMixin, DeleteView):
    model = Result
    success_url = reverse_lazy("result_list")


#Analysis
class AnalysisListView(ListView):
    model = Analysis

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fig, ax = plt.subplots()
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        ax.plot(x, y)

        flike = io.BytesIO()
        fig.savefig(flike)
        b64 = base64.b64encode(flike.getvalue()).decode()
        context['chart'] = b64
        return context