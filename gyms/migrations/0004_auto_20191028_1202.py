# Generated by Django 2.2.3 on 2019-10-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0003_auto_20191028_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='admins',
            field=models.ManyToManyField(to='users.User'),
        ),
    ]
