# Generated by Django 2.2.3 on 2019-10-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_auto_20191024_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='Service_name',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='package_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
