# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=4)),
                ('lastname', models.CharField(max_length=6)),
                ('wholename', models.CharField(max_length=11)),
                ('projects', models.IntegerField(verbose_name=3)),
                ('favorite_food', models.CharField(max_length=20)),
                ('least_favorite_pet', models.CharField(max_length=10)),
                ('favorite_pet', models.CharField(max_length=15)),
                ('current_residence', models.CharField(max_length=50)),
                ('current_location', models.CharField(max_length=30)),
                ('favorite_color', models.CharField(max_length=10)),
                ('favorite_duet', models.CharField(max_length=20)),
                ('favorite_student', models.CharField(max_length=6)),
                ('quality_of_jokes', models.CharField(max_length=50)),
                ('favorite_coding_laguage', models.CharField(max_length=20)),
                ('joeltaddie', models.BooleanField()),
                ('least_favorite_food', models.CharField(max_length=20)),
                ('least_favorite_color', models.CharField(max_length=10)),
                ('planned_app', models.CharField(max_length=20)),
                ('mood', models.CharField(max_length=20)),
            ],
        ),
    ]