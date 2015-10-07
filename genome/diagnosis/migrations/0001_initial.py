# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('disease_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('profile_id', models.IntegerField()),
                ('genome', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Snp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('chromosome', models.CharField(max_length=2)),
                ('chromosome_position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SnpDisease',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('snp_name', models.CharField(max_length=32)),
                ('disease_id', models.IntegerField()),
                ('rate', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
    ]
