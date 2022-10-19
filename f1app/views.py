
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
import io, base64
import numpy as np
import pandas as pd
import seaborn as sb

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

        #load the data and assign columns
        results = pd.read_csv(r"f1app\data\results.csv",sep = ',',encoding='utf-8')
        races = pd.read_csv(r"f1app\data\races.csv",sep = ';',encoding='utf-8')
        drivers = pd.read_csv(r"f1app\data\drivers.csv",sep = ',',encoding='utf-8')
        constructors = pd.read_csv(r"f1app\data\constructors.csv",sep = ',',encoding='utf-8')

        #merge datasets
        df = pd.merge(results, races[["raceId", "year", "name", "round"]], on="raceId", how="left")
        df = pd.merge(df, drivers[["driverId", "driverRef", "nationality"]], on = "driverId", how="left")
        df = pd.merge(df, constructors[["constructorId", "name", "nationality"]], on="constructorId", how="left")

        #drop, rename, rearrange coloumns
        df.drop(["number", "position", "positionText", "laps", "fastestLap", "statusId", "resultId", "raceId", "driverId", "constructorId"], axis=1, inplace = True)
        df.rename(columns={"rank":"fastestLapRank", "name_x":"gpName", "nationality_x":"driverNationality", "name_y":"constructorName", "nationality_y":"constructorNationality", "driverRef":"driver"}, inplace = True)
        df = df[["year", "gpName", "round", "driver", "constructorName", "grid", "positionOrder", "points", "time", "milliseconds", "fastestLapRank", "fastestLapTime", "fastestLapSpeed", "driverNationality", "constructorNationality"]]

        #drop incomplete seasons
        df = df[df["year"]!=2021]
        df = df[df["year"]!=2022]

        #sort values
        df = df.sort_values(by=["year", "round", "positionOrder"], ascending = [False, True, True])

        #replace \N values
        df.time.replace("\\N", np.nan, inplace = True)
        df.milliseconds.replace("\\N", np.nan, inplace = True)
        df.fastestLapRank.replace("\\N", np.nan, inplace = True)
        df.fastestLapTime.replace("\\N", np.nan, inplace = True)
        df.fastestLapSpeed.replace("\\N", np.nan, inplace = True)

        #change datatypes
        df.fastestLapSpeed = df.fastestLapSpeed.astype(float)
        df.fastestLapRank = df.fastestLapRank.astype(float)
        df.milliseconds = df.milliseconds.astype(float)

        #reset index
        df.reset_index(drop=True, inplace = True)

        sb.set_palette("Set3")
        plt.rcParams["figure.figsize"]=10,6

        driver_winner = df.loc[df["positionOrder"]==1].groupby("driver")["positionOrder"].count().sort_values(ascending=False).to_frame().reset_index()

        sb.barplot(data=driver_winner, y ="driver", x="positionOrder", color="green", alpha=0.8)

        top10Drivers = driver_winner.head(10)
        sb.barplot(data = top10Drivers, y = "driver", x="positionOrder", color="blue", alpha = 0.8, linewidth=.8, edgecolor="black")
        plt.title("Top 10 Gp Winners")
        plt.ylabel("Drivers")
        plt.xlabel("Number of Wins")
        fig = plt.figure()

        flike = io.BytesIO()
        fig.savefig(flike)
        b64 = base64.b64encode(flike.getvalue()).decode()
        context['chart'] = b64

        return context