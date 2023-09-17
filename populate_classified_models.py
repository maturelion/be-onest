import os
import json
import django
import uuid

# Set up Django's environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# Import your models
from classifieds.models import Classified
from locations.models import Country, State, City

# Specify the path to your JSON data file
json_file_path = 'classifiedData.json'


def populate_models_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for item in data:
            # Extract data for the Classified model
            try:
                title = item.get('title')
                description = item.get('description')
                country = item.get('country')
                state = item.get('state')
                city = item.get('city')
                is_hot = item.get('is_hot')

                country_instance = Country.objects.get(name=country)
                state_instance = State.objects.get(
                    name=state, country=country_instance)
                city_instance = City.objects.get(
                    name=city, state=state_instance)

                classified, created = Classified.objects.get_or_create(
                    title=title,
                    description=description,
                    country=country_instance,
                    state=state_instance,
                    city=city_instance,
                    is_hot=is_hot,
                )
            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    populate_models_from_json(json_file_path)
