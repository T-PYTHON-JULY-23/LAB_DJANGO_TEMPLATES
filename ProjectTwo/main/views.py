from django.shortcuts import render
import datetime
import random
import string
import secrets
from django.http import HttpRequest,HttpResponse


def views_today(request:HttpRequest):
    context = {'day':datetime.date.today()}
    return render(request, 'main/today.html', context)

def views_password(request:HttpRequest):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet= letters+digits+special_chars
    pwd_length = 10
    pwd =" for i in range(pwd_length): pwd +=".join(secrets.choice(alphabet))
    print(pwd)
    context = {'password':pwd}
    return render(request, 'main/random_password.html', {'date:now'})

def views_games(request:HttpRequest):
    games = ["Game01","Game02","Game03"]
    context = {'Myfavgames':games}
    return render(request, 'main/games.html', context)

# Create your views here.
