from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('today/', views.date_view, name='date_view'),
    path('random/password/', views.random_password,name='random_password'),
    path('favs/games/', views.fav_movies, name='fav_movies'),
]
