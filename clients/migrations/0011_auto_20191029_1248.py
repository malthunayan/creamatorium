# Generated by Django 2.2.3 on 2019-10-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20191029_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('F', 'Famale'), ('M', 'Male')], max_length=1, verbose_name='Gender'),
        ),
    ]
