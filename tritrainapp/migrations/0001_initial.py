# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dst_Name', models.CharField(max_length=200)),
                ('dst_Swim', models.IntegerField(default=0)),
                ('dst_Cicle', models.IntegerField(default=0)),
                ('dst_Run', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_StartSwimTime', models.DateTimeField()),
                ('res_EndSwimTime', models.DateTimeField()),
                ('res_StartCicleTime', models.DateTimeField()),
                ('res_EndCicleTime', models.DateTimeField()),
                ('res_StartRunTime', models.DateTimeField()),
                ('res_EndRunTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sportsman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sm_Name', models.CharField(max_length=200)),
                ('sm_Distance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tritrainapp.Distance')),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='res_Sportsman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tritrainapp.Sportsman'),
        ),
    ]
