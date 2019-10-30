# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField
from users.models import User
from branches.models import Branch
from gyms.models import Gym

# Create your models here.
class Employee(models.Model):
    word = RegexValidator(regex='^[-\w\s]*$', message='Name must not contain special characters', code='invalid_name')
    alphabetic = RegexValidator(regex='^[^0-9_]*$', message='Name must be alphabetic', code='invalid_name')
    gym = models.ForeignKey(Gym,on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50, validators=[word, alphabetic])
    second_name = models.CharField(max_length=50,validators=[word, alphabetic], blank=True, null=True)
    last_name = models.CharField(max_length=50,validators=[word, alphabetic])
    social_id = models.CharField(max_length=255, unique=True)
    social_id_img = models.CharField(max_length=255, null=True, blank=True)
    passport_number = models.CharField(max_length=255, unique=True)
    passport_img = models.CharField(max_length=255, null=True, blank=True)
    nationality = CountryField(blank=True,null=True)
    mobile = models.CharField(max_length=20,unique=True)
    emergency_contact = models.CharField(max_length=20,null=True,blank=True);
    email = models.CharField(max_length=50,unique=True,null=True,blank=True)
    GENDER_CHOICES={
        ('M',"Male"),
        ('F', "Famale")
    }
    gender = models.CharField(verbose_name='Gender',max_length=1,choices=GENDER_CHOICES)
    birth_date = models.DateField(verbose_name="Birth Date",blank=True,null=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    driving_license_expiry = models.DateField(blank=True,null=True)
    visa_expiry = models.DateField(blank=True,null=True)
    hire_date = models.DateField(blank=True,null=True)
    resign_date = models.DateField(blank=True,null=True)
    branches = models.ManyToManyField(Branch,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,unique=True)
    permissions = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.first_name

