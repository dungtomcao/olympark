from django.shortcuts import render
from datetime import datetime
from .models import Plant, Animal, Habitat
# Create your views here.
def index(request):
    return render(request, 'parkapp/index.html')

def plants(request):
    plant_list=Plant.objects.all()
    return render(request, 'parkapp/plants.html', {'plant_list' : plant_list})

def animals(request):
    animal_list=Animal.objects.all()
    return render(request, 'parkapp/animals.html', {'animal_list' : animal_list})

def habitats(request):
    habitat_list=Habitat.objects.all()
    return render(request, 'parkapp/habitats.html', {'habitat_list' : habitat_list})