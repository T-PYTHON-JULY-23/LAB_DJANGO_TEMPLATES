from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("today/", views.today_date, name="date_view"),
    path("random/password/", views.random_pass, name="passowrd_view"),
    path("favs/games/", views.fav_games, name="games_view")
]