from django.urls import path
from . import views
name_app='main'
urlpatterns = [
    path('today/',views.today,name="date" ),
    path('random/password/',views.random_pass,name="password" ),
]