from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Plant, Animal, Habitat
from django.urls import reverse, reverse_lazy
from .forms import HabitatForm, AnimalForm, PlantForm
from django.contrib.auth.decorators import login_required
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
This is because Habitat table and Animal/Plant table has a
one to many relationship. 1 habitat links to many plants/animals
Currently, animal/plant of id 1 only links to habitat of id 1, and
this is similar to id 2,3,4,...

I don't know how to fix this problem, please help '''

@login_required
def newhabitat(request):
    form=HabitatForm
    if request.method=='POST':
        form=HabitatForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=HabitatForm()
    else:
        form=HabitatForm()
    return render(request, 'parkapp/newhabitat.html', {'form' : form})

@login_required
def newanimal(request):
    form=AnimalForm
    if request.method=='POST':
        form=AnimalForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AnimalForm()
    else:
        form=AnimalForm()
    return render(request, 'parkapp/newanimal.html', {'form' : form})

@login_required
def newplant(request):
    form=PlantForm
    if request.method=='POST':
        form=PlantForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=PlantForm()
    else:
        form=PlantForm()
    return render(request, 'parkapp/newplant.html', {'form' : form})

def loginmessage(request):
    return render(request,'registration/loginmessage.html')

def logoutmessage(request):
    return render(request,'registration/logoutmessage.html')