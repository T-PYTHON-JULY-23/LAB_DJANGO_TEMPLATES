from django.shortcuts import render
import datetime
import random
from django.http import HttpRequest , HttpResponse


def today(request):
    now = datetime.datetime.now()
    return render(request , 'main/today.html' ,{'date' : now})

def random_password(request):
      characters = '1234567opk'
      password = ''.join(random.choice(characters) for i in range(17))
      return render(request, 'main/random_password.html', {'password': password})    

def favorite_games(request):
    games = ['INSID', 'SKY', 'PLATO', 'LASTDAY']
    return render(request, 'main/favorite_games.html', {'games': games})