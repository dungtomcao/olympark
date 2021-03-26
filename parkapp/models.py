from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Habitat(models.Model):
    habitatname=models.CharField(max_length=255)
    habitatdescription=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.habitatname

    class Meta:
        db_table='habitat'

class Plant(models.Model):
    plantname=models.CharField(max_length=255)
    plantsciname=models.CharField(max_length=255)
    plantdescription=models.TextField()
    planthabitat=models.ForeignKey(Habitat, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()

    def __str__(self):
        return self.plantname

    class Meta:
        db_table='plant'

class Animal(models.Model):
    animalname=models.CharField(max_length=255)
    animalsciname=models.CharField(max_length=255)
    animaldescription=models.TextField()
    animalhabitat=models.ForeignKey(Habitat, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()

    def __str__(self):
        return self.animalname

    class Meta:
        db_table='animal'
