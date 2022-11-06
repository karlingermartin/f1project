from django import forms
from f1app.models import Driver, Constructor, Circuit, Races, Result
from django.utils.translation import gettext_lazy as _


class DriverForm(forms.ModelForm):

    class Meta():
        model = Driver
        fields = ("forename", "surname", "driver_nationality")
        labels = {
            "driver_nationality": _("Nationality"),
            "race_wins": _("Race Wins"),
            "championships": _("Championships"),
        }


class ConstructorForm(forms.ModelForm):

    class Meta():
        model = Constructor
        fields = ("constructor_name", "constructor_nationality")
        labels = {
            "constructor_name": _("Name"),
            "constructor_nationality": _("Nationality"),
            "constructor_race_wins": _("Race Wins"),
        }


class CircuitForm(forms.ModelForm):

    class Meta():
        model = Circuit
        fields = ("circuit_name", "circuit_city", "circuit_country")
        labels = {
            "circuit_name": _("Name"),
            "circuit_city": _("City"),
            "circuit_country": _("Country"),
        }


class RacesForm(forms.ModelForm):

    class Meta():
        model = Races
        fields = ("race_year", "round", "circuit", "race_name", "date")
        labels = {
            "circuit": _("Circuit ID"),
        }


class ResultForm(forms.ModelForm):

    class Meta():
        model = Result
        fields = ("race", "driver", "constructor", "grid",
                  "position_order", "points", "laps", "rank")
        labels = {
            "race": _("Race ID"),
            "driver": _("Driver ID"),
            "constructor": _("Constructor ID"),
            "position_order": _("Position"),
        }
