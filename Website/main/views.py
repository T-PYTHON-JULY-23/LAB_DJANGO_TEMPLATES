from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
import random
import string

def today(request : HttpRequest):
    today_date = datetime.datetime.now()
    context = {"today" :today_date}
    return render(request, "main/today.html",context)
# Create your views here.

def random_password(request : HttpRequest):
       random_pass = random.choices(string.ascii_letters+string.digits+string.punctuation, k=15)
       random_pass_string = "".join(random_pass)
       context = {"pass" : random_pass_string}
       return render(request, "main/random_password.html",context)

def games(request : HttpRequest):

    games = ['pubg','call of duty','CrossFire', 'Minecraft. Minecraft. ']
    context = {"games" : games}

    return render(request, "main/games.html", context)