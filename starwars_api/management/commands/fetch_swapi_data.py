import urllib3
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from starwars_api.models import Planet, Species, Film, Character, Vehicle, Starship
from starwars_api.utils import parse_int

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Command(BaseCommand):
    def get_object_by_url(self, model, url, cache):
        if url in cache:
            return cache[url]
        try:
            data = requests.get(url, verify=False).json()
            obj = model.objects.filter(name=data.get("name")).first()
            cache[url] = obj
            return obj
        except Exception:
            return None

    def fetch_all(self, endpoint):
        url = f"{settings.SWAPI_BASE}/{endpoint}/"
        results = []
        while url:
            try:
                response = requests.get(url, verify=False)
                response.raise_for_status()
                data = response.json()
                results.extend(data["results"])
                url = data["next"]
            except requests.RequestException as e:
                self.stderr.write(self.style.ERROR(f"API request failed: {e}"))
                return []
        return results

    def set_related(self, instance, related_name, model, urls, cache):
        related_objs = [
            self.get_object_by_url(model, url, cache)
            for url in urls
        ]
        related_objs = [obj for obj in related_objs if obj]
        getattr(instance, related_name).set(related_objs)

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching data from SWAPI...")
        cache = {}

        self.stdout.write("Fetching all planets...")
        for data in self.fetch_all("planets"):
            Planet.objects.update_or_create(
                name=data["name"],
                defaults={
                    "rotation_period": data["rotation_period"],
                    "orbital_period": data["orbital_period"],
                    "diameter": data["diameter"],
                    "climate": data["climate"],
                    "gravity": data["gravity"],
                    "terrain": data["terrain"],
                    "surface_water": data["surface_water"],
                    "population": data["population"],
                },
            )
        self.stdout.write("Fetched planets")

        self.stdout.write("Fetching all species...")
        for data in self.fetch_all("species"):
            planet = self.get_object_by_url(Planet, data.get("homeworld"), cache) if data.get("homeworld") else None
            species, _ = Species.objects.update_or_create(
                name=data["name"],
                defaults={
                    "classification": data["classification"],
                    "designation": data["designation"],
                    "average_height": parse_int(data.get("average_height")),
                    "skin_colors": data["skin_colors"],
                    "hair_colors": data["hair_colors"],
                    "eye_colors": data["eye_colors"],
                    "average_lifespan": parse_int(data.get("average_lifespan")),
                    "homeworld": planet,
                    "language": data["language"],
                },
            )
            self.set_related(species, "people", Character, data["people"], cache)
        self.stdout.write("Fetched species")

        self.stdout.write("Fetching all films...")
        for data in self.fetch_all("films"):
            film, _ = Film.objects.update_or_create(
                title=data["title"],
                defaults={
                    "episode_id": data["episode_id"],
                    "opening_crawl": data["opening_crawl"],
                    "director": data["director"],
                    "producer": data["producer"],
                    "release_date": data["release_date"],
                },
            )
            self.set_related(film, "planets", Planet, data["planets"], cache)
            self.set_related(film, "characters", Character, data["characters"], cache)
            self.set_related(film, "starships", Starship, data["starships"], cache)
            self.set_related(film, "vehicles", Vehicle, data["vehicles"], cache)
            self.set_related(film, "species", Species, data["species"], cache)
        self.stdout.write("Fetched films")

        self.stdout.write("Fetching all characters...")
        for data in self.fetch_all("people"):
            planet = self.get_object_by_url(Planet, data.get("homeworld"), cache) if data.get("homeworld") else None
            Character.objects.update_or_create(
                name=data["name"],
                defaults={
                    "height": data["height"],
                    "mass": data["mass"],
                    "hair_color": data["hair_color"],
                    "skin_color": data["skin_color"],
                    "eye_color": data["eye_color"],
                    "birth_year": data["birth_year"],
                    "gender": data["gender"],
                    "homeworld": planet,
                },
            )
        self.stdout.write("Fetched characters")

        self.stdout.write("Fetching all vehicles...")
        for data in self.fetch_all("vehicles"):
            vehicle, _ = Vehicle.objects.update_or_create(
                name=data["name"],
                defaults={
                    "model": data["model"],
                    "manufacturer": data["manufacturer"],
                    "cost_in_credits": data["cost_in_credits"],
                    "length": data["length"],
                    "max_atmosphering_speed": data["max_atmosphering_speed"],
                    "crew": data["crew"],
                    "passengers": data["passengers"],
                    "cargo_capacity": data["cargo_capacity"],
                    "consumables": data["consumables"],
                    "vehicle_class": data["vehicle_class"],
                },
            )
            self.set_related(vehicle, "pilots", Character, data["pilots"], cache)
        self.stdout.write("Fetched vehicles")

        self.stdout.write("Fetching all starships...")
        for data in self.fetch_all("starships"):
            starship, _ = Starship.objects.update_or_create(
                name=data["name"],
                defaults={
                    "model": data["model"],
                    "manufacturer": data["manufacturer"],
                    "cost_in_credits": data["cost_in_credits"],
                    "length": data["length"],
                    "max_atmosphering_speed": data["max_atmosphering_speed"],
                    "crew": data["crew"],
                    "passengers": data["passengers"],
                    "cargo_capacity": data["cargo_capacity"],
                    "consumables": data["consumables"],
                    "hyperdrive_rating": data["hyperdrive_rating"],
                    "MGLT": data["MGLT"],
                    "starship_class": data["starship_class"],
                },
            )
            self.set_related(starship, "pilots", Character, data["pilots"], cache)
        self.stdout.write("Fetched starships")

        self.stdout.write(self.style.SUCCESS("All SWAPI data successfully imported."))
