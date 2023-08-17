from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import datetime
import random
import string

# Create your views here.
def today(request: HttpRequest):
    date =datetime.date.today()
    today_date={"today_date":date}
    return render(request,"main/today.html",today_date )

def random_pass(request: HttpRequest):
    Password =''.join(random.choice(string.ascii_letters) for i in range(10))
    random_pass={"password":Password}
    return render(request,"main/random.html",random_pass )

def game(request: HttpRequest):
    game_fav =["crash","soduku","find out","gardenscapes"]
    game={"games":game_fav}
    return render(request,"main/game.html",game )