from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Pictures

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def index(request):
    Picture = Pictures.objects.all()
    return render(request, 'all_art/index.html',{'Picture':Picture})

