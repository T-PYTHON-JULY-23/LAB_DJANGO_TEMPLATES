from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
import secrets
import string

# Create your views here.




def date_today(request:HttpRequest):
    today = date.today()
    context ={"date":today}
    return render(request ,'main/today_date.html', context)
    

def random_password(request:HttpRequest):
    letters = string.ascii_letters #lowercase and uppercase
    digits = string.digits #numbers from 0 t0 10
    special_chars = string.punctuation #special characters

    alphabet = letters + digits + special_chars


    pwd_length = 10
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    print(pwd)
    context = {'pass':pwd}
    return render(request , 'main/random_password.html', context)


def fave_game(request:HttpRequest):
    games = ['pupg','Minecraft','Call of duty']
    context = {'favgame':games}
    return render(request, 'main/favs_games.html', context)
