from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def date(request:HttpRequest):
    today = date.today
    context ={"date":today}
    return render(request ,'main/date_today.html', context)
    
