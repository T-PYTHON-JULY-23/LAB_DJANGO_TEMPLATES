from django.urls import path
from . import views
name_app='main'
urlpatterns = [
    path('today/',views.today_date,name="date" ),
    path('random/password/',views.random_password,name="password" ),
    path('favs/games/',views.favs_game,name="games" ),
]