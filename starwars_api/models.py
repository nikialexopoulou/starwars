from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200, unique=True)
    episode_id = models.IntegerField(null=True, blank=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    characters = models.ManyToManyField('Character', related_name='films', blank=True)
    planets = models.ManyToManyField('Planet', related_name='films', blank=True)
    starships = models.ManyToManyField('Starship', related_name='films', blank=True)
    vehicles = models.ManyToManyField('Vehicle', related_name='films', blank=True)
    species = models.ManyToManyField('Species', related_name='films', blank=True)


class Starship(models.Model):
    name = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    cost_in_credits = models.CharField(max_length=50, null=True, blank=True)
    length = models.CharField(max_length=50, null=True, blank=True)
    max_atmosphering_speed = models.CharField(max_length=50, null=True, blank=True)
    crew = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.CharField(max_length=50, null=True, blank=True)
    cargo_capacity = models.CharField(max_length=50, null=True, blank=True)
    consumables = models.CharField(max_length=50, null=True, blank=True)
    hyperdrive_rating = models.CharField(max_length=10, null=True, blank=True)
    MGLT = models.CharField(max_length=10, null=True, blank=True)
    starship_class = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    pilots = models.ManyToManyField('Character', related_name='starships', blank=True)


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    mass = models.CharField(max_length=10, null=True, blank=True)
    hair_color = models.CharField(max_length=50, null=True, blank=True)
    skin_color = models.CharField(max_length=50, null=True, blank=True)
    eye_color = models.CharField(max_length=50, null=True, blank=True)
    birth_year = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    homeworld = models.ForeignKey(
        'Planet',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='residents'
    )
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class Planet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rotation_period = models.CharField(max_length=50, null=True, blank=True)
    orbital_period = models.CharField(max_length=50, null=True, blank=True)
    diameter = models.CharField(max_length=50, null=True, blank=True)
    climate = models.CharField(max_length=100, null=True, blank=True)
    gravity = models.CharField(max_length=100, null=True, blank=True)
    terrain = models.CharField(max_length=100, null=True, blank=True)
    surface_water = models.CharField(max_length=50, null=True, blank=True)
    population = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    name = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    cost_in_credits = models.CharField(max_length=50, null=True, blank=True)
    length = models.CharField(max_length=50, null=True, blank=True)
    max_atmosphering_speed = models.CharField(max_length=50, null=True, blank=True)
    crew = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.CharField(max_length=50, null=True, blank=True)
    cargo_capacity = models.CharField(max_length=50, null=True, blank=True)
    consumables = models.CharField(max_length=50, null=True, blank=True)
    vehicle_class = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    pilots = models.ManyToManyField('Character', blank=True, related_name='vehicles_piloted')


class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    classification = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    average_height = models.IntegerField(null=True, blank=True)
    skin_colors = models.CharField(max_length=255, null=True, blank=True)
    hair_colors = models.CharField(max_length=255, null=True, blank=True)
    eye_colors = models.CharField(max_length=255, null=True, blank=True)
    average_lifespan = models.IntegerField(null=True, blank=True)
    homeworld = models.ForeignKey(
        'Planet',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='species_planet'
    )
    language = models.CharField(max_length=100, null=True, blank=True)
    people = models.ManyToManyField(Character, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
