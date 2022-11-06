from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Driver
import os
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'f1app/drivers.csv'), 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                driver = {
                    "pk": row["driverId"],
                    "forename": row["forename"],
                    "surname": row["surname"],
                    "driver_nationality": row["nationality"]
                }
                Driver.objects.create(**driver)
