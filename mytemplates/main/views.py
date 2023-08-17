from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from datetime import date
import string
import secrets
# Create your views here.

def home_page(request: HttpRequest):

    return render(request, 'home.html')


def today_page(request:HttpResponse):
    today = date.today()
    today1 = {"today" : today }

    return render(request, "todaydate.html", today1)

def password_page(request:HttpResponse):
    password=secrets.token_urlsafe(10)
    final={"random_password":password}
    return render(request,"randompassword.html",final)
def games_page(request: HttpRequest):
    FavGames = ["Football","Fifa","Resident Evil"]
    mylist = {"list_of_FavGames":FavGames}
    return render(request, 'games.html',mylist)