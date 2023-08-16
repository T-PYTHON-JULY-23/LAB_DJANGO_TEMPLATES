from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("today/", views.today, name="today"),
    path("random_password/", views.random_password, name="random_password"),
    path("games/", views.games, name="games"),
]