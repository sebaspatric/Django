from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.

def create(request):
    #todo crear elementos
    #place = Place(name = request.POST['name'], address = request.POST['address'])
    place = Place(name="Lugar 1", address = "Calle 1")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()

    return HttpResponse(restaurant.place.name)


