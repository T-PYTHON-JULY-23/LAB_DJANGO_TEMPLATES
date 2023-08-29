from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from datetime import date
# Create your views here.


def dateview (request:HttpRequest):
    today = date.today
    context ={"date":today}
    return render(request ,"main/date.html",context )

def passwordview (request:HttpRequest):
    context= {"password":"lam98765"}
    return render(request,"main/password.html",context)

def favgames(request:HttpRequest):
    games = ["Ludo","Monopoly","Crash","HomeEscapes","Redecor"]
    context={"faveGames":games}
    return render(request,"main/favGames.html",context)