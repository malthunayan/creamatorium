import django
from users.models import User
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Gym(models.Model):
    company_name  = models.CharField(max_length=255)
    gym_name = models.CharField(max_length=255)
    logo = models.URLField()
    country = CountryField()
    currency_symbol = models.CharField(max_length=5)
    tax = models.FloatField(default=0)
    admins = models.ManyToManyField(User)
    phone = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    date_modfied = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.gym_name
