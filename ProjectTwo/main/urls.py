from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('today/', views.today , name = 'views_today'),
    path('random/password/'   , views.password , name ='views_password'),
    path('favs/games/',views.games, name='views_games'),
]