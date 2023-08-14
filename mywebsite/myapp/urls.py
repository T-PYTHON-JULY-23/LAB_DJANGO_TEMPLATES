from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('today/' , views.today , name='today'),
    path('random/password/' , views.random_password , name='random_password'),
    path('favs/games/', views.favorite_games , name='favorite_games'),
]

