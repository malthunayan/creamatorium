# Generated by Django 2.2.3 on 2019-10-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0006_auto_20191025_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='extra_days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='membership',
            name='extra_sessions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
