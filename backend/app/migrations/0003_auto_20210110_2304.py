# Generated by Django 3.1.3 on 2021-01-10 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210110_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TourCatalog',
            new_name='Tour',
        ),
    ]