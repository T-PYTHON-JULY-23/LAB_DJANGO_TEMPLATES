from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
import secrets
import string

# Create your views here.
def today_view(request : HttpRequest):
    context={"date":datetime.datetime.now()}

    return render(request, "main/today.html",context)

def random_pass_view(request : HttpRequest): 
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation
  alphabet = letters + digits + special_chars
  pwd_length = 12
  pwd = ''
  for i in range(pwd_length):
   pwd += ''.join(secrets.choice(alphabet))
  print(pwd)
  context= {"password":pwd}
  return render(request, "main/random_pass.html",context)


def favs_games_view(request : HttpRequest):
    fav_games= ['FIFA','UNO','CRASH','JACARO']
 
    context= {"fav_games":fav_games}

    return render(request, "main/favs_games.html",context)

