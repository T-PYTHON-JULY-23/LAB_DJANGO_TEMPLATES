from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import datetime
import random 
import string

# Create your views here.
def hello_view(request):
    return HttpResponse('<h1>Hello view<1>')


def today_view(request):
    context={'day':datetime.date.today()}
    return render(request ,'main/today.html',context)


def password_view(request):
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    password = "" 
    for i in range(0,6):  
        password = password + random.choice(list_of_chars)    
    
    context={'password':password}
    
    
    return render(request ,'main/password.html',context)

def games_view(request):

    games=['Game1','Game2','Game3']
    context={'games':games}

    return render(request , 'main/games.html' , context)
    
    