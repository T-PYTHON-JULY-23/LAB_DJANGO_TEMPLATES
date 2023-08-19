from django.urls import path
from . import views


app_name= "main"

urlpatterns= [
    path("today/", views.today_view, name="today"),
    path("random/password/", views.random_password_view, name="random_password"),
    path("favs/games/", views.favorite_games_view, name="favorite_games"),

]

