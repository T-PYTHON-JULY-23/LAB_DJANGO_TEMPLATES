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
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = 12
    password = ''
    for i in range(pwd_length):
        password += ''.join(random.choice(alphabet))
    print(password)
    context = {"password" :password}
    return render(request, "main/random_password.html",context)

def games(request : HttpRequest):

    games = ['pubg','call of duty','CrossFire', 'Minecraft. Minecraft. ']
    context = {"games" : games}

    return render(request, "main/games.html", context)