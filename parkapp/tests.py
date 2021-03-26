from django.test import TestCase
from .models import Animal, Plant, Habitat
from django.contrib.auth.models import User
import datetime
from django.urls import reverse, reverse_lazy
from .views import index, animals, plants, habitats, habitatdetails

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

class indextest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)

class gethabitat(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('habitats'))
       self.assertEqual(response.status_code, 200)

class habitatdetailstest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')
        self.habitat=Habitat.objects.create(habitatname='habitat 1', habitatdescription='hab des', user=self.user)
        self.plant=Plant.objects.create(plantname='plant 1', plantsciname='name', 
        plantdescription='desc', planthabitat=self.habitat, user=self.user, dateentered=datetime.date(2021, 12, 30))

    def test_habitat_details_success(self):
        response = self.client.get(reverse('habitatdetails', args=(self.habitat.id,)))
        self.assertEqual(response.status_code, 200)

class getanimaltest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('animals'))
       self.assertEqual(response.status_code, 200)

class getplanttest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('plants'))
       self.assertEqual(response.status_code, 200)

class gethabitattest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('habitats'))
       self.assertEqual(response.status_code, 200)
        