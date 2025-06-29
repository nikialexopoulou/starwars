from django.urls import path

from starwars_api.views import CharacterListView, FilmListView, StarshipListView

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='character-list'),
    path('films/', FilmListView.as_view(), name='film-list'),
    path('starships/', StarshipListView.as_view(), name='starship-list'),
]
