from turtle import position
from django.db import models
from django.urls import reverse
import computed_property
from django_matplotlib import MatplotlibFigureField
import matplotlib.pyplot as plt

# Create your models here.


class Driver(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    driver_nationality = models.CharField(max_length=100)
    race_wins = computed_property.ComputedIntegerField(
        compute_from='race_wins')
    championships = computed_property.ComputedIntegerField(
        compute_from='championships')

    @property
    def race_wins(self):
        c = Result.objects.filter(position_order=1).filter(
            driver_id=f"{self.id}").count()
        return c

    @property
    def championships_old(self):
        champions = {}
        for r in Result.objects.all():
            year, driver_id, points = r.race.race_year, r.driver_id, r.points
            if year not in champions:
                champions[year] = {}
            if driver_id not in champions[year]:
                champions[year][driver_id] = []
            champions[year][driver_id].append(points)
        points_per_years = {}
        for year in champions.keys():
            points_per_years[year] = {}
        for year, item in champions.items():
            for driver_id, points in item.items():
                points_per_years[year][driver_id] = sum(points)
        champ = 0
        for year, table in points_per_years.items():
            if self.id in table:
                if max(table.values()) == table[self.id]:
                    champ += 1
        print(points_per_years)
        return champ

    @property
    def championships(self):
        qry = """
                select count(d) as c, 1 as id from 
	            (select max(s), y, d
	            from
		        (select  
			        f1app_result.driver_id as d, 
			        sum(f1app_result.points) as s, 
			        f1app_races.race_year as y
		        from f1app_result join f1app_races on f1app_result.race_id = f1app_races.id
		        group by f1app_result.driver_id, f1app_races.race_year
		        ) as t
		        group by y)
		        where d = %s;
            """

        print(f'Driver ID = {self.id}')
        for champ in Result.objects.raw(qry, [self.id]):
            print(champ.c)
        return champ.c

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse("driver_detail", kwargs={"pk": self.pk})


class Constructor(models.Model):
    constructor_name = models.CharField(max_length=100, unique=True)
    constructor_nationality = models.CharField(max_length=100)
    constructor_race_wins = computed_property.ComputedIntegerField(
        compute_from='constructor_race_wins')

    @property
    def constructor_race_wins(self):
        return Result.objects.filter(position_order=1).filter(constructor_id=f"{self.id}").count()

    def __str__(self):
        return self.constructor_name

    def get_absolute_url(self):
        return reverse("constructor_detail", kwargs={"pk": self.pk})


class Circuit(models.Model):
    circuit_name = models.CharField(max_length=100)
    circuit_city = models.CharField(max_length=100)
    circuit_country = models.CharField(max_length=100)

    def __str__(self):
        return self.circuit_name

    def get_absolute_url(self):
        return reverse("circuit_detail", kwargs={"pk": self.pk})


class Races(models.Model):
    race_year = models.PositiveIntegerField()
    round = models.PositiveIntegerField()
    circuit = models.ForeignKey(
        Circuit, related_name="races", on_delete=models.CASCADE)
    race_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.race_name

    def get_absolute_url(self):
        return reverse("race_detail", kwargs={"pk": self.pk})


class Result(models.Model):
    race = models.ForeignKey(
        Races, related_name="results", on_delete=models.CASCADE)
    driver = models.ForeignKey(
        Driver, related_name="results", on_delete=models.CASCADE)
    constructor = models.ForeignKey(
        Constructor, related_name="results", on_delete=models.CASCADE)
    grid = models.PositiveIntegerField()
    position_order = models.PositiveIntegerField()
    points = models.FloatField()
    laps = models.PositiveIntegerField()
    rank = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse("result_detail", kwargs={"pk": self.pk})


class Analysis(models.Model):
    figure = MatplotlibFigureField(
        figure='my_figure', verbose_name='figure', silent=True)

    def __str__(self):
        return self.figure

    def get_absolute_url(self):
        return reverse("analysis_list", kwargs={"pk": self.pk})
