from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Races
import os
import csv
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'f1app/races.csv'), 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                race = {
                    "pk": row["raceId"],
                    "race_year": row["year"],
                    "round": row["round"],
                    "circuit_id": row["circuitId"],
                    "race_name": row["name"],
                    "date": datetime.datetime.strptime(row["date"], "%Y.%m.%d"),
                }
                print(race)
                Races.objects.create(**race)
