from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
import random
import string

def date_view(request : HttpRequest):
    todayDate = datetime.datetime.now()
    context = {"today" :todayDate}
    return render(request, "main/date.html",context)


def random_view(request : HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    context = {"password" :password}
    return render(request, "main/random.html",context)


def games_view(request : HttpRequest):

    favGames = ['omori','story of seasons','genshin impact','animal crossing']
    context = {"games" : favGames}

    return render(request, "main/games.html", context)