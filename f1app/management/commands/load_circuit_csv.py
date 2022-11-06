from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Circuit
import os
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'f1app/data/circuits.csv'), 'r', encoding="latin-1") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                circuit = {
                    "pk": row["circuitId"],
                    "circuit_name": row["name"],
                    "circuit_city": row["location"],
                    "circuit_country": row["country"],
                }
                print(circuit)
                Circuit.objects.create(**circuit)
