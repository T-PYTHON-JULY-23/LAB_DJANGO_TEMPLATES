from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
#from datetime import date
import random
import string



def home_view(request : HttpRequest):
    
    return render(request, "main/home.html")


def today_date(request:HttpRequest):
    
    date_of_day =datetime.date.today()
    todaydate={"date":date_of_day}
    return render(request,"main/today.html",todaydate )

def random_pass(request:HttpRequest):
    strings = string.printable
    password ={ "random_pass":''.join(random.choice(strings) for i in range(8))}

    return render(request, "main/random_pass.html", password)


def fav_games(request:HttpRequest):
    favorate_games = { "games": ["water sort","wordle","ball sort","call of duty"]}

    return render(request,"main/fav_games.html",favorate_games)
