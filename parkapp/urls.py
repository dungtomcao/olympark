from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('plants/', views.plants, name='plants'),
    path('animals/', views.animals, name='animals'),
    path('habitats/', views.habitats, name='habitats'),
    path('habitatdetails/<int:id>', views.habitatdetails, name='habitatdetails'), 
    path('newhabitat/', views.newhabitat, name='newhabitat'),
    path('newanimal/', views.newanimal, name='newanimal'),
    path('newplant/', views.newplant, name='newplant'),

]
