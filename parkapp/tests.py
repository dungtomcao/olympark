from django.test import TestCase
from .models import Animal, Plant, Habitat
from django.contrib.auth.models import User
import datetime
from django.urls import reverse, reverse_lazy

# Create your tests here.

class habitattest(TestCase):
    def setUp(self):
        self.hab=Habitat(habitatname='habitat 1')

    def test_habstring(self):
        self.assertEqual(str(self.hab), 'habitat 1')

    def test_tablename(self):
        self.assertEqual(str(Habitat._meta.db_table), 'habitat')

class animaltest(TestCase):
    def setUp(self):
        self.animal=Animal(animalname='animal 1')
        self.user=User(username='Tim')
        self.animalhabitat=Habitat(habitatname='habitat1', habitatdescription='habitatdes1')

    def test_animalstring(self):
        self.assertEqual(str(self.animal), 'animal 1')

    def test_tablename(self):
        self.assertEqual(str(Animal._meta.db_table), 'animal')

class planttest(TestCase):
    def setUp(self):
        self.plant=Plant(plantname='plant 1')
        self.user=User(username='Tim')
        self.planthabitat=Habitat(habitatname='habitat1', habitatdescription='habitatdes1')

    def test_plantstring(self):
        self.assertEqual(str(self.plant), 'plant 1')

    def test_tablename(self):
        self.assertEqual(str(Plant._meta.db_table), 'plant')

