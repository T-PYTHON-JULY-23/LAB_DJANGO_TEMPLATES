from django.urls import path
from . import views

app_name = 'main'

urlpatterns= [
    path('today/', views.date_today, name='date'),
    path('favs/games/', views.fave_game, name='fave_game'),
    path('random/password/',views.random_password, name='random_password' )
]

