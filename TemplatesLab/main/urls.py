from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("today/", views.today_view, name="today_view"),
    path("random/password/", views.random_pass_view, name="random_pass_view"),
    path("favs/games/", views.favs_games_view, name="favs_games_view")
]