
import datetime
import random
from django.shortcuts import render
from django.http import HttpResponse ,HttpRequest

def today_view(request:HttpRequest):
    today = datetime.date.today()
    return render(request, 'website/today.html', {'today': today})


def random_password_view(request:HttpRequest):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    length = 12
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return render(request, 'website/random_password.html', {'random_password': random_password})

def favorite_games_view(request:HttpRequest):
    favorite_games = ['Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5']
    return render(request, 'website/favorite_games.html', {'favorite_games': favorite_games})

