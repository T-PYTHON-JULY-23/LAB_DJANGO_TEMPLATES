from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path("home/",views.home_page,name="home_page"),
    path("todaydate/",views.today_page,name="today_page"),
    path("random/password/",views.password_page,name="password_page"),
    path("favs/games/",views.games_page,name="games_page"),
]