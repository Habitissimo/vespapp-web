from django.core.management import BaseCommand
import json

from api.models import Location


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data/locations.json', 'r') as f:
            location_str = f.read()
            locations = json.loads(location_str)

        for location in locations:
            l = Location()
            l.lat = location.get('lat')
            l.lng = location.get('lng')
            l.name = location.get('name')
            l.save()

