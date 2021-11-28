from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Pictures,Category,Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    Picture = Pictures.objects.all().order_by('-id')
    return render(request, 'all_art/index.html',{'Picture':Picture})

def search_results(request):

    if 'pictures' in request.GET and request.GET["pictures"]:
        search_term = request.GET.get("pictures")
        searched_pictures = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_art/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all_art/search.html',{"message":message})

def pictures(request,pictures_id):
    try:
        pictures = Pictures.objects.get(id = pictures_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all_art/pictures.html", {"pictures":pictures})

def location(request,location_id):
    location = Location.objects.all()
    # pictures = Pictures.objects.get(id=location_id)
    # loc = Location.objects.get(id=location_id)
    return render (request,'all_art/navbar.html',{'location': location})



