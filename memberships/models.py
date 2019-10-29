import django
from django.db import models
from clients.models import Client
from service.models import Service,Package,Price
from branches.models import Branch
# Create your models here.


class Membership(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    client_name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=255,unique=True)
    invoice_date =models.DateField(default=django.utils.timezone.now)
    duration = models.PositiveIntegerField(default=0)
    sessions = models.PositiveIntegerField(default=0)
    extra_days = models.PositiveIntegerField(default=0)
    extra_sessions = models.PositiveIntegerField(default=0)
    start_date = models.DateField(verbose_name='start')
    sessions_valid_to = models.DateField(verbose_name='sessions_valid')
    end_date = models.DateField(verbose_name='end')
    notes = models.CharField(max_length=1000,blank=True,null=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    service_name = models.CharField(max_length=255)
    package = models.ForeignKey(Package, on_delete=models.PROTECT)
    package_name = models.CharField(max_length=255)
    price = models.ForeignKey(Price, on_delete=models.PROTECT)
    price_name = models.CharField(max_length=255)
    original_price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    paid=models.FloatField(default=0)
    balance = models.FloatField(default=0)
    create_by = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.CharField(max_length=50, blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    date_modified = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.client_name


class MembershipPayments(models.Model):
    membership = models.ForeignKey(Membership,on_delete=models.PROTECT)
    cash_amount=models.FloatField(default=0)
    debit_amount=models.FloatField(default=0)
    debit_refrence = models.IntegerField(default=0)
    credit_amount=models.FloatField(default=0)
    credit_refrence = models.IntegerField(default=0)
    def __str__(self):
        return self.membership.client_name