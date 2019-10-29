# Generated by Django 2.2.3 on 2019-10-28 09:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('branches', '0001_initial'),
        ('gyms', '0005_auto_20191028_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name must not contain special characters', regex='^[-\\w\\s]*$'), django.core.validators.RegexValidator(code='invalid_name', message='Name must be alphabetic', regex='^[^0-9_]*$')])),
                ('second_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name must not contain special characters', regex='^[-\\w\\s]*$'), django.core.validators.RegexValidator(code='invalid_name', message='Name must be alphabetic', regex='^[^0-9_]*$')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name must not contain special characters', regex='^[-\\w\\s]*$'), django.core.validators.RegexValidator(code='invalid_name', message='Name must be alphabetic', regex='^[^0-9_]*$')])),
                ('social_id', models.CharField(max_length=255, unique=True)),
                ('social_id_img', models.CharField(blank=True, max_length=255, null=True)),
                ('passport_number', models.CharField(max_length=255, unique=True)),
                ('passport_img', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('mobile', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Famale')], max_length=1, verbose_name='Gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('driving_license_expiry', models.DateField(blank=True, null=True)),
                ('visa_expiry', models.DateField(blank=True, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('resign_date', models.DateField(blank=True, null=True)),
                ('permissions', models.CharField(blank=True, max_length=50, null=True)),
                ('branches', models.ManyToManyField(blank=True, null=True, to='branches.Branch')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gyms.Gym')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User', unique=True)),
            ],
        ),
    ]
