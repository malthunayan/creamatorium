# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField
from branches.models import Branch

# Create your models here.
from gyms.models import Gym


class Client(models.Model):
    word = RegexValidator(regex='^[-\w\s]*$', message='Name must not contain special characters', code='invalid_name')
    alphabetic = RegexValidator(regex='^[^0-9_]*$', message='Name must be alphabetic', code='invalid_name')
    first_name = models.CharField(max_length=50, validators=[word, alphabetic])
    second_name = models.CharField(max_length=50,validators=[word, alphabetic], blank=True, null=True)
    last_name = models.CharField(max_length=50,validators=[word, alphabetic])
    civil_id = models.CharField(max_length=255,unique=True)
    nationality = CountryField(blank=True,null=True)
    mobile = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=50,unique=True)
    gym = models.ForeignKey(Gym,on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    GENDER_CHOICES={
        ('M',"Male"),
        ('F', "Famale")
    }
    gender = models.CharField(verbose_name='Gender',max_length=1,choices=GENDER_CHOICES)
    birth_date = models.DateField(verbose_name="Birth Date",blank=True,null=True)

    referred_by = models.CharField(max_length=50,blank=True,null=True)
    relatives = models.CharField(max_length=50,blank=True,null=True)
    # user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    create_by = models.CharField(max_length=50,blank=True,null=True)
    date_created = models.CharField(max_length=50,blank=True,null=True)
    modified_by = models.CharField(max_length=50,blank=True,null=True)
    date_modified = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.first_name

