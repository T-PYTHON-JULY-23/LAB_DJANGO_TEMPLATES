from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date

import random
import string

# Create your views here.

def date_view(request: HttpRequest) -> HttpResponse:

    today = date.today()


    return render(request, 'index/today.html', {"today": today})

def random_password(request: HttpRequest) -> HttpResponse:

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for chr in range(10))

    return render(request, 'passwordPage/password.html', {"password": password})

def fav_movies(request: HttpRequest)-> HttpResponse:
    context = {
        "movies": [
            "movie1",
            "movie2",
            "movie3",
            "movie4",
        ]
    }
    return render(request, 'favMovies/fav_movies.html', context)

