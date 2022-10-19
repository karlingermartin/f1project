from copyreg import constructor
from django.core.management.base import BaseCommand
from django.conf import settings
from f1app.models import Constructor
import os, csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'f1app/constructors.csv'), 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                constructor = {
                    "pk": row["constructorId"],
                    "constructor_name": row["name"],
                    "constructor_nationality": row["nationality"],
                }
                print(constructor)
                Constructor.objects.create(**constructor)#constructor_id = row[0], constructor_name=row[1], constructor_nationality=row[2])