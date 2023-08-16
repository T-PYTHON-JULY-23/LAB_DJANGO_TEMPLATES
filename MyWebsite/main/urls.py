from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("today/", views.today, name="today"),
    path("random/password/", views.password, name="password"),
    path("favs/games", views.favs_games, name="favs_games"),
]

