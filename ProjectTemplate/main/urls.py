from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('date/',views.date_of_today, name="views.date_of_today"),
    path('pass/',views.random_of_pass,name="random_of_pass"),
    path('game/',views.favorit_game, name="favorit_game")
]