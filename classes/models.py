import django
from django.db import models
from branches.models import Branch
from employees.models import Employee
from clients.models import Client
# Create your models here.
class Days(models.Model):
    name= models.CharField(max_length=15)
    def __str__(self):
        return self.name

class CoachClasses(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    coach = models.ForeignKey(Employee,on_delete=None)
    days = models.ManyToManyField(Days)
    capacity = models.PositiveSmallIntegerField(default=0)
    vip_capacity = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ClassSession(models.Model):
     coach_class = models.ForeignKey(CoachClasses,on_delete=models.CASCADE)
     date = models.DateField()
     start = models.TimeField()
     end = models.TimeField()
     is_locked = models.BooleanField(default=False)
     date_locked = models.DateTimeField()
     capacity = models.PositiveSmallIntegerField(default=0)
     vip_capacity = models.PositiveSmallIntegerField(default=0)

     def __str__(self):
         self.coach_class.name +" - Class Session"


class ClientsAttendance(models.Model):
    client= models.ForeignKey(Client,on_delete=models.CASCADE)
    class_session = models.ForeignKey(ClassSession,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_present = models.BooleanField(default=True)
    added_by = models.ForeignKey(Employee,on_delete=None)
    date_created = models.DateField(default=django.utils.timezone.now)
    date_modified = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        self.client.name +" - "+ self.class_session.coach_class.name