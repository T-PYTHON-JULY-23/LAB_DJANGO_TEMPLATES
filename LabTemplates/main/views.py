from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string







def today_view(request: HttpRequest):
    today = date.today()
    context={"today": today}
    return render(request, "main/today.html", context)

def random_password_view(request:HttpRequest):
    password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    context={"password": password}
    return render(request, "main/random_password.html", context)

def favorite_games_view(request:HttpRequest):
    games = ["puzzle", "crash", "driver"]  
    context={"games": games}
    return render(request, "main/favorite_games.html", context)

