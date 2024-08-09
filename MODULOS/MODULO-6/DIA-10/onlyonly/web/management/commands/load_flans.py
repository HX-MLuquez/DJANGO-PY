import os
import json
from django.core.management.base import BaseCommand
from web.models import Flan
from django.db import transaction

class Command(BaseCommand):
    help = 'Load flans data from JSON file if the table is empty'

    def handle(self, *args, **kwargs):
        if not Flan.objects.exists():
            file_path = os.path.join(os.path.dirname(__file__), 'flans.json')
            with open(file_path) as file:
                flans_data = json.load(file)
                flans = [
                    Flan(
                        flan_uuid=flan['flan_uuid'],
                        name=flan['name'],
                        description=flan['description'],
                        image_url=flan['image_url'],
                        slug=flan['slug'],
                        is_private=bool(flan['is_private'])
                    )
                    for flan in flans_data
                ]
                with transaction.atomic():
                    Flan.objects.bulk_create(flans)
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('Table is not empty, no data loaded'))

#! IMPORTANTE
#* Para cargar la data a la db sqlite, ejecutar ->
# python manage.py load_flans
# 