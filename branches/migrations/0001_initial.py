# Generated by Django 2.2.3 on 2019-10-22 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gyms', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=1000)),
                ('coordinates', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('timezone', models.TimeField(blank=True, null=True)),
                ('tax', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modfied', models.DateTimeField(default=django.utils.timezone.now)),
                ('gym', models.ForeignKey(on_delete=None, to='gyms.Gym')),
                ('service', models.ManyToManyField(blank=True, null=True, to='service.Service')),
            ],
        ),
    ]
