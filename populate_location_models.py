import os
import json
import django

# Set up Django's environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# Import your models
from locations.models import Country, State, City

# Specify the path to your JSON data file
json_file_path = 'locationData.json'

def populate_models_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for item in data:
            # Extract data for the Country model
            country_data = item.get('country')
            country, created = Country.objects.get_or_create(name=country_data['name'])

            # Extract data for the State model
            for state_data in item.get('states', []):
                state, created = State.objects.get_or_create(name=state_data['name'], country=country)

                # Extract data for the City model
                for city_name in state_data.get('cities', []):
                    City.objects.get_or_create(name=city_name, state=state)

if __name__ == "__main__":
    populate_models_from_json(json_file_path)
