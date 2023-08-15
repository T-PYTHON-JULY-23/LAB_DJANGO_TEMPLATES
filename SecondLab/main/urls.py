from django.urls import path
from . import views 
app_name = "main"

urlpatterns =[
    path("",views.dateview,name="date"),
    path("login/",views.passwordview,name="passwordview"),
    path("faveoritGames/",views.favgames,name="favgames")
]