# Generated by Django 3.1.4 on 2020-12-13 13:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=50)),
                ('airline_country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookedTours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_adults', models.IntegerField()),
                ('number_of_children', models.IntegerField()),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('airline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.airlines')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('is_visa', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_address', models.CharField(max_length=50)),
                ('number_of_rooms', models.IntegerField()),
                ('type_of_food', models.IntegerField()),
                ('price_for_night', models.DecimalField(decimal_places=2, max_digits=8)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cities')),
            ],
        ),
        migrations.CreateModel(
            name='Insurances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dates_of_insurance', models.DateField()),
                ('value_of_insurance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('access_right', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tourists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.BooleanField()),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('citizenship', models.CharField(max_length=50)),
                ('document_data', models.CharField(max_length=50)),
                ('document_term', models.DateField()),
                ('date_of_issue_of_document', models.DateField()),
                ('document_issued_by', models.CharField(max_length=50)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.clients')),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bookedtours')),
                ('type_of_document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.typeofdocuments')),
            ],
        ),
        migrations.CreateModel(
            name='TourCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tour_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.countries')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotels')),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.countries'),
        ),
        migrations.AddField(
            model_name='bookedtours',
            name='insurance_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.insurances'),
        ),
        migrations.AddField(
            model_name='bookedtours',
            name='tour_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tourcatalog'),
        ),
    ]