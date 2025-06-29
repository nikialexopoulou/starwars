from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from starwars_api.filters import CharacterFilter, FilmFilter, StarshipFilter
from starwars_api.models import Character, Film, Starship
from starwars_api.serializers import CharacterSerializer, FilmSerializer, StarshipSerializer


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CharacterFilter

class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilmFilter

class StarshipListView(generics.ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StarshipFilter
