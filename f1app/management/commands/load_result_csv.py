from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Result
import os, csv
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'f1app/results.csv'), 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                #print(row)
                try:
                    rank = int(row["rank"])
                except ValueError:
                    rank = None
                result = {
                    "pk": row["resultId"],
                    "race_id": row["raceId"],
                    "driver_id": row["driverId"],
                    "constructor_id": row["constructorId"],
                    "grid": row["grid"],
                    "position_order": row["positionOrder"],
                    "points": row["points"],
                    "laps": row["laps"],
                    "rank": rank,
                }
                #print(result)
                Result.objects.create(**result) #, race_year=row[1], round=row[2], circuit_id=row[3], race_name=row[4], date=row[5])
