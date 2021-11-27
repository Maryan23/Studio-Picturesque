from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Pictures

# Create your views here.
def index(request):
    Picture = Pictures.objects.all()
    return render(request, 'all_art/index.html',{'Picture':Picture})

def search_results(request):

    if 'pictures' in request.GET and request.GET["pictures"]:
        search_term = request.GET.get("pictures")
        searched_pictures = Pictures.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all_art/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_art/search.html',{"message":message})

