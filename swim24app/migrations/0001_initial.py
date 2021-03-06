# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-12 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbls24ActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('al_user', models.CharField(max_length=64)),
                ('al_Timestamp', models.DateTimeField()),
                ('al_Action', models.IntegerField(default=0)),
                ('al_Comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbls24Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dst_Name', models.CharField(max_length=200)),
                ('dst_SwimDuration', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tbls24Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_StartTime', models.DateTimeField(null=True)),
                ('res_SwimLaps', models.IntegerField(default=0)),
                ('res_FinishTime', models.DurationField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbls24Sportsman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sm_Name', models.CharField(max_length=200)),
                ('sm_Distance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swim24app.tbls24Distance')),
            ],
        ),
        migrations.AddField(
            model_name='tbls24results',
            name='res_Sportsman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swim24app.tbls24Sportsman'),
        ),
    ]
