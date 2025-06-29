from rest_framework import serializers
from .models import Film, Starship, Character, Planet, Vehicle, Species


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    homeworld = PlanetSerializer(read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class StarshipSerializer(serializers.ModelSerializer):
    pilots = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = Starship
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    pilots = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'


class SpeciesSerializer(serializers.ModelSerializer):
    homeworld = PlanetSerializer(read_only=True)
    people = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = Species
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)
    planets = PlanetSerializer(many=True, read_only=True)
    starships = StarshipSerializer(many=True, read_only=True)
    vehicles = VehicleSerializer(many=True, read_only=True)
    species = SpeciesSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = '__all__'
