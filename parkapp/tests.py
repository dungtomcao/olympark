from django.test import TestCase
from .models import Animal, Plant, Habitat
from django.contrib.auth.models import User
import datetime
from django.urls import reverse, reverse_lazy
from .views import index, animals, plants, habitats, habitatdetails
from .forms import HabitatForm, AnimalForm, PlantForm

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

class newhabitatform(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='tom', password='P@ssw0rd1')

    def test_habitatform_empty(self):
        data={
        'habitatname': '', 
        'habitatdescription':'',
        'user': ''
        }
        form = HabitatForm(data)
        self.assertFalse(form.is_valid())

    def test_habitatform(self):
        data={
            'habitatname': 'habitat1', 
            'habitatdescription':'habitat desc',
            'user': self.user
        }
        form = HabitatForm(data)
        self.assertTrue(form.is_valid())

class newanimalform(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='tom', password='P@ssw0rd1')
        self.habitat=Habitat.objects.create(habitatname='habitat 1', habitatdescription='hab des', user=self.user)

    def test_animalform_empty(self):
        data={
        'animalname': '', 
        }
        form = AnimalForm(data)
        self.assertFalse(form.is_valid())

    def test_animalform(self):
        data={
            'animalname': 'animal1', 
            'animalsciname':'animal name',
            'animaldescription': 'des',
            'animalhabitat':self.habitat,
            'user': self.user,
            'dateentered': datetime.date(2020, 12, 30),
        }
        form = AnimalForm(data)
        self.assertTrue(form.is_valid())

class newplantform(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='tom', password='P@ssw0rd1')
        self.habitat=Habitat.objects.create(habitatname='habitat 1', habitatdescription='hab des', user=self.user)

    def test_plantform_empty(self):
        data={
        'plantname': '', 
        }
        form = AnimalForm(data)
        self.assertFalse(form.is_valid())

    def test_plantform(self):
        data={
            'plantname': 'plant1', 
            'plantsciname':'plant name',
            'plantdescription': 'des',
            'planthabitat':self.habitat,
            'user': self.user,
            'dateentered': datetime.date(2020, 12, 30),
        }
        form = PlantForm(data)
        self.assertTrue(form.is_valid())

class new_habitat_auth_test(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='tom', password='P@ssw0rd1')
        self.habitat=Habitat.objects.create(habitatname='habitat 1', habitatdescription='hab des', user=self.user)
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newhabitat'))
        self.assertRedirects(response, '/accounts/login/?next=/parkapp/newhabitat/')

    def test_logged_in_uses_correct_template(self):
        login=self.client.login(username='tom', password='P@ssw0rd1')
        response=self.client.get(reverse('newhabitat'))
        self.assertEqual(str(response.context['user']), 'tom')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parkapp/newhabitat.html')

class new_animal_auth_test(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='tom', password='P@ssw0rd1')
        self.habitat=Habitat.objects.create(habitatname='habitat 1', habitatdescription='hab des', user=self.user)
        self.animal=Animal.objects.create(
            animalname= 'animal1', 
            animalsciname='animal name',
            animaldescription= 'des',
            animalhabitat=self.habitat,
            user= self.user,
            dateentered= datetime.date(2020, 12, 30),
        )
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newanimal'))
        self.assertRedirects(response, '/accounts/login/?next=/parkapp/newanimal/')

    def test_logged_in_uses_correct_template(self):
        login=self.client.login(username='tom', password='P@ssw0rd1')
        response=self.client.get(reverse('newanimal'))
        self.assertEqual(str(response.context['user']), 'tom')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parkapp/newanimal.html')

class new_plant_auth_test(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='tom', password='P@ssw0rd1')
        self.habitat=Habitat.objects.create(habitatname='habitat 1', habitatdescription='hab des', user=self.user)
        self.plant=Plant.objects.create(
            plantname = 'plant1', 
            plantsciname ='plant name',
            plantdescription = 'des',
            planthabitat = self.habitat,
            user = self.user,
            dateentered = datetime.date(2020, 12, 30),
        )
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newplant'))
        self.assertRedirects(response, '/accounts/login/?next=/parkapp/newplant/')

    def test_logged_in_uses_correct_template(self):
        login=self.client.login(username='tom', password='P@ssw0rd1')
        response=self.client.get(reverse('newplant'))
        self.assertEqual(str(response.context['user']), 'tom')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parkapp/newplant.html')