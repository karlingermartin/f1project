from django import forms
from f1app.models import Driver, Constructor, Circuit
from django.utils.translation import gettext_lazy as _

class DriverForm(forms.ModelForm):

    class Meta():
        model = Driver
        fields = ("forename", "surname", "driver_nationality",  "race_wins", "championships")
        labels = {
            "driver_nationality": _("Nationality"),
            "race_wins" : _("Race Wins"),
            "championships" : _("Championships"),
        }


class ConstructorForm(forms.ModelForm):

    class Meta():
        model = Constructor
        fields = ("constructor_name", "constructor_nationality", "constructor_race_wins")
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
