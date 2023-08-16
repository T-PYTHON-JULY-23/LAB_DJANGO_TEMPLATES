from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
import random
import string

def date_of_today(request : HttpRequest):
    date = datetime.datetime.now()
    context = {"today" :date}
    return render(request, "main/date.html",context)
# Create your views here.

def random_of_pass(request : HttpRequest):
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
    return render(request, "main/psaa.html",context)

def favorit_game(request : HttpRequest):
    
    games = ['pubg','call of duty','sims', 'hey dey']
    context = {"games" : games}

    return render(request, "main/game.html", context)