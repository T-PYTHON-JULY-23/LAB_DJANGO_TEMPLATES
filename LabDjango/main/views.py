from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from datetime import datetime
import random
import string



day1=datetime.now()
day=day1.strftime('%A')
contaxt={"date":day}

def today_view(request:HttpRequest):
    return render(request, "main/today.html", contaxt)




password=10
char=string.ascii_letters+string.digits+"@"+"!"+"&"+"-"+"_"
password=''.join(random.choice(char) for _ in range(random.randint(8,password)))
content={"random":password}


def random_view(request:HttpRequest):
    return render(request, "main/random.html", content)


my_favorite_games=["Red Dead Redemption 2","Battlefield 4","Bloodborne"]
list_games={"games":my_favorite_games}

def games_view(request:HttpRequest):
    return render(request, "main/games.html", list_games)
