from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Races
import os, csv
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
                    #"date": row["date"],
                    "date": datetime.datetime.strptime(row["date"], "%Y.%m.%d"),
                }
                print(race)
                Races.objects.create(**race) #, race_year=row[1], round=row[2], circuit_id=row[3], race_name=row[4], date=row[5])
