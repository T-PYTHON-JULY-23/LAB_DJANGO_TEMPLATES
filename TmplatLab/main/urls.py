from django.urls import path
from . import views


app_name='main'
urlpatterns = [
    path('',views.hello_view,name='hello_view'),
    path('today/',views.today_view,name='today_view'),
    path('random/password/',views.password_view,name='password_view'),
    path('favs/games/',views.games_view,name='games_view'),

    
    
]
