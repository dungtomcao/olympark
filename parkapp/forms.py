from django import forms 
from .models import Animal, Habitat, Plant

class HabitatForm(forms.ModelForm):
    class Meta:
        model=Habitat
        fields='__all__'

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields='__all__'

class AnimalForm(forms.ModelForm):
    class Meta:
        model=Animal
        fields='__all__'