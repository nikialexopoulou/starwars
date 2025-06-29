from unittest.mock import patch, MagicMock
from django.core.management import call_command
from django.test import TestCase
from requests import RequestException
from rest_framework.test import APITestCase

from starwars_api.models import Planet, Species, Film, Character, Vehicle, Starship

class StarWarsViewsTests(APITestCase):
    def setUp(self):
        film = Film.objects.create(
            title="A New Hope",
            episode_id=4,
            opening_crawl="It is a period of civil war...",
            director="George Lucas",
            producer="Gary Kurtz, Rick McCallum",
            release_date="1977-05-25"
        )
        planet = Planet.objects.create(
            name="Tatooine",
            rotation_period="23",
            orbital_period="304",
            diameter="10465",
            climate="arid",
            gravity="1 standard",
            terrain="desert",
            surface_water="1",
            population="200000"
        )
        film.planets.add(planet)

    def test_list_films(self):
        response = self.client.get('/api/films/')
        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        results = json_data.get("results", json_data)

        self.assertTrue(any(f.get("title") == "A New Hope" for f in results))

    def test_filter_films_by_title(self):
        response = self.client.get("/api/films/?title=A New Hope")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        results = data.get("results", data)

        self.assertTrue(all("A New Hope" in f.get("title", "") for f in results))


class FetchSWAPIDataCommandTests(TestCase):
    def setUp(self):
        Planet.objects.create(name="Tatooine")

    @patch('starwars_api.management.commands.fetch_swapi_data.requests.get')
    def test_fetch_swapi_data_success(self, mock_get):
        def side_effect(url, *args, **kwargs):
            if "planets" in url:
                return MagicMock(status_code=200, json=lambda: {
                    "results": [{
                        "name": "Tatooine",
                        "rotation_period": "23",
                        "orbital_period": "304",
                        "diameter": "10465",
                        "climate": "arid",
                        "gravity": "1 standard",
                        "terrain": "desert",
                        "surface_water": "1",
                        "population": "200000"
                    }],
                    "next": None
                })
            elif "species" in url:
                return MagicMock(status_code=200, json=lambda: {
                    "results": [{
                        "name": "Human",
                        "classification": "mammal",
                        "designation": "sentient",
                        "average_height": "180",
                        "skin_colors": "caucasian, black, asian, hispanic",
                        "hair_colors": "blonde, brown, black, red",
                        "eye_colors": "brown, blue, green, hazel, grey, amber",
                        "average_lifespan": "120",
                        "homeworld": "https://swapi.dev/api/planets/1/",
                        "language": "Galactic Basic",
                        "people": []
                    }],
                    "next": None
                })
            elif "films" in url:
                return MagicMock(status_code=200, json=lambda: {
                    "results": [{
                        "title": "A New Hope",
                        "episode_id": 4,
                        "opening_crawl": "It is a period of civil war...",
                        "director": "George Lucas",
                        "producer": "Gary Kurtz, Rick McCallum",
                        "release_date": "1977-05-25",
                        "planets": ["https://swapi.dev/api/planets/1/"],
                        "characters": [],
                        "starships": [],
                        "vehicles": [],
                        "species": []
                    }],
                    "next": None
                })
            elif "people" in url:
                return MagicMock(status_code=200, json=lambda: {
                    "results": [{
                        "name": "Luke Skywalker",
                        "height": "172",
                        "mass": "77",
                        "hair_color": "blond",
                        "skin_color": "fair",
                        "eye_color": "blue",
                        "birth_year": "19BBY",
                        "gender": "male",
                        "homeworld": "https://swapi.dev/api/planets/1/"
                    }],
                    "next": None
                })
            elif "vehicles" in url:
                return MagicMock(status_code=200, json=lambda: {
                    "results": [{
                        "name": "Sand Crawler",
                        "model": "Digger Crawler",
                        "manufacturer": "Corellia Mining Corporation",
                        "cost_in_credits": "150000",
                        "length": "36.8",
                        "max_atmosphering_speed": "30",
                        "crew": "46",
                        "passengers": "30",
                        "cargo_capacity": "50000",
                        "consumables": "2 months",
                        "vehicle_class": "wheeled",
                        "pilots": []
                    }],
                    "next": None
                })
            elif "starships" in url:
                return MagicMock(status_code=200, json=lambda: {
                    "results": [{
                        "name": "Death Star",
                        "model": "DS-1 Orbital Battle Station",
                        "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
                        "cost_in_credits": "1000000000000",
                        "length": "120000",
                        "max_atmosphering_speed": "n/a",
                        "crew": "342953",
                        "passengers": "843342",
                        "cargo_capacity": "1000000000000",
                        "consumables": "3 years",
                        "hyperdrive_rating": "4.0",
                        "MGLT": "10",
                        "starship_class": "Deep Space Mobile Battlestation",
                        "pilots": []
                    }],
                    "next": None
                })
            else:
                raise ValueError(f"Unexpected URL: {url}")

        mock_get.side_effect = side_effect

        call_command('fetch_swapi_data')

        self.assertTrue(Film.objects.filter(title="A New Hope").exists())
        self.assertTrue(Planet.objects.filter(name="Tatooine").exists())
        self.assertTrue(Species.objects.filter(name="Human").exists())
        self.assertTrue(Character.objects.filter(name="Luke Skywalker").exists())
        self.assertTrue(Vehicle.objects.filter(name="Sand Crawler").exists())
        self.assertTrue(Starship.objects.filter(name="Death Star").exists())

    @patch("starwars_api.management.commands.fetch_swapi_data.requests.get")
    def test_fetch_swapi_data_api_failure(self, mock_get):
        mock_get.side_effect = RequestException("SWAPI is down")

        try:
            call_command("fetch_swapi_data")
        except RequestException:
            self.fail("fetch_swapi_data should handle RequestException without crashing")
