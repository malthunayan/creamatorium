# Generated by Django 2.2.3 on 2019-12-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0004_auto_20191207_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('being', 'being'), ('new', 'new'), ('pickup', 'pickup'), ('ready', 'ready')], max_length=6, verbose_name='status'),
        ),
    ]
