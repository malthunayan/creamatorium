import django
from django.db import models
from gyms.models import Gym

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    date_modfied = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.id) + " - " + self.name


class Package(models.Model):
    name = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    is_active = models.BooleanField(default=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    date_modfied = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.service.id) + " - " + str(self.service.name) + " - " + self.name


class Price(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    sessions = models.PositiveIntegerField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    date_modfied = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.package.service.id) + " - "+ self.package.name + " - "+ self.name

