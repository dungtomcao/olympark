from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('plants/', views.plants, name='plants'),
    path('animals/', views.animals, name='animals'),
    path('habitats/', views.habitats, name='habitats'),
]
