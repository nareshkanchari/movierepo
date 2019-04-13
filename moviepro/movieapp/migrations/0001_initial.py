# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-11 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Movie_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('theater_name', models.CharField(max_length=50)),
                ('show_time', models.CharField(max_length=50)),
                ('select_seats', models.IntegerField()),
                ('select_date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hindi_Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=300)),
                ('director_name', models.CharField(max_length=50)),
                ('Hero_name', models.CharField(max_length=50)),
                ('Heroiene_name', models.CharField(max_length=50)),
                ('producer_name', models.CharField(max_length=50)),
                ('released_date', models.DateField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telugu_Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=300)),
                ('director_name', models.CharField(max_length=50)),
                ('Hero_name', models.CharField(max_length=50)),
                ('Heroiene_name', models.CharField(max_length=50)),
                ('producer_name', models.CharField(max_length=50)),
                ('released_date', models.DateField(max_length=50)),
            ],
        ),
    ]