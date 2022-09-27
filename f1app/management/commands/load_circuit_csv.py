from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Circuit
import os, csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'f1app/circuits.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                Circuit.objects.create(circuit_id = row[0], circuit_name=row[1], circuit_city=row[2], circuit_country=row[3])