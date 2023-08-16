from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
from datetime import datetime
import random

# Create your views here.

def home_view(request: HttpRequest):
    content = "This is home page"
    return HttpResponse(content)


def today(request: HttpRequest):

    today_date = datetime.now()

    return render(request,"main/today.html",{"today_date":today_date})


def password(request: HttpRequest):
     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
     password = "" 
     for i in range(10):  
        password+= random.choice(chars)    
     return render(request,"main/password.html",{'password':password})



def favs_games(request: HttpRequest):
    games = ['Padel', 'Billiardo', 'Plato', 'Lodo']
    return render(request, 'main/favs_games.html',{"games": games} )

