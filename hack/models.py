from django.db import models

# Create your models here.
class Order(models.Model):
    status_CHOICES={
        ('pickup',"pickup"),
        ('being', "being"),
        ('new', "new"),
        ('ready', "ready"),
    }
    status = models.CharField(verbose_name='status',max_length=6,choices=status_CHOICES)
    description = models.CharField(max_length=5000)
    def __str__(self):
        return str(self.id)