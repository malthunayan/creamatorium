import django
from django.db import models
from gyms.models import Gym
from service.models import Service
from django_countries.fields import CountryField

# Create your models here.
class Branch(models.Model):
    gym = models.ForeignKey(Gym,on_delete=None)
    name = models.CharField(max_length=255,unique=True)
    address = models.CharField(max_length=1000)
    coordinates = models.CharField(max_length=500)
    phone = models.CharField(max_length=20,unique=True)
    timezone = models.TimeField(null=True,blank=True)
    tax = models.CharField(max_length=255)
    service = models.ManyToManyField(Service,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    date_modfied = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return  self.gym.gym_name +" - "+self.name
