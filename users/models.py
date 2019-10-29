import django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class userManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have an username")

        userData = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        userData.set_password(password)
        userData.save(using=self._db)
        return userData

    def create_superuser(self, email, username, password):
        userData = self.create_user(
            username=username,
            password=password,
            email=self.normalize_email(email),
        )
        userData.is_admin = True
        userData.is_active = True
        userData.is_staff = True
        userData.save(using=self._db)
        return userData


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    second_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name='email', unique=True, max_length=100)
    mobile = models.IntegerField(unique=True, null=True, blank=True)
    emergency_mobile = models.IntegerField(blank=True, null=True)
    photo = models.URLField(default='any')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    height = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_gym_owner = models.BooleanField(default=False)
    is_gym_employee = models.BooleanField(default=False)
    is_gym_client = models.BooleanField(default=False)
    email_verifed = models.BooleanField(default=False)
    mobile_verifed = models.BooleanField(default=False)
    activation_token = models.CharField(max_length=255,blank=True,null=True)
    token_expiration = models.DateTimeField(blank=True,null=True)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    date_modfied = models.DateTimeField(default=django.utils.timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password',]

    objects = userManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_Label):
        return True
