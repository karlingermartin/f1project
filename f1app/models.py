#from computedfields.models import ComputedFieldsModel, computed, compute
from django.db import models
#from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True, default="0")
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    driver_nationality = models.CharField(max_length=100)
    race_wins = models.PositiveIntegerField("auth.User")
    championships = models.PositiveIntegerField("auth.User")   

    #@computed(models.CharField(max_length=100), depends=[('self', ['race_wins'])])
    #def get_race_wins(self):
    #    return Driver.objects.filter(Result.position_order == 1).count()

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse("driver_detail", kwargs={"pk": self.pk})


class Constructor(models.Model):
    constructor_id = models.AutoField(primary_key=True, default="0")
    constructor_name = models.CharField(max_length=100, unique=True)
    constructor_nationality = models.CharField(max_length=100)
    constructor_race_wins = models.PositiveIntegerField("auth.User")

    def __str__(self):
        return self.constructor_name

    def get_absolute_url(self):
        return reverse("constructor_detail", kwargs={"pk": self.pk})


class Circuit(models.Model): 
    circuit_id = models.AutoField(primary_key=True, default="0")
    circuit_name = models.CharField(max_length=100)
    circuit_city = models.CharField(max_length=100)
    circuit_country = models.CharField(max_length=100)

    def __str__(self):
        return self.circuit_name

    def get_absolute_url(self):
        return reverse("circuit_detail", kwargs={"pk": self.pk})
   

class Races(models.Model):
    race_id = models.AutoField(primary_key=True, default="0")
    race_year = models.PositiveIntegerField()
    round = models.PositiveIntegerField()
    circuit_id_2 = models.ForeignKey(Circuit, related_name="races", on_delete=models.CASCADE)
    race_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.race_name

    def get_absolute_url(self):
        return reverse("race_detail", kwargs={"pk": self.pk})


class Result(models.Model):
    result_id = models.AutoField(primary_key=True, default="0")
    race_id = models.ForeignKey(Races, related_name="results", on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, related_name="results", on_delete=models.CASCADE)
    constructor_id = models.ForeignKey(Constructor, related_name="results", on_delete=models.CASCADE)
    grid = models.PositiveIntegerField()
    position_order = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    laps = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return self.result_id

    def get_absolute_url(self):
        return reverse("result_detail", kwargs={"pk": self.pk})



