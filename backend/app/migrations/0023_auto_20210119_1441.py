# Generated by Django 3.1.3 on 2021-01-19 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210119_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedtour',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='bookedtour',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='document',
            name='birthdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
