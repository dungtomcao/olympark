from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Plant, Animal, Habitat
from django.urls import reverse_lazy
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

def habitatdetails(request, id):
    habitat=get_object_or_404(Habitat, pk=id)
    return render(request, 'parkapp/habitatdetails.html', {'habitat' : habitat})

'''The habitatdetails link in other tables' views don't link correctly 
for example, in animals table, the animal has id of 1 
but the habitat of that animal has id of 3 in habitats table
{url 'habitatdetails' id=a.id} returns habitat of id 1 instead of 3

I don't know how to fix this problem, please help '''