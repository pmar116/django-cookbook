# Generated by Django 3.0.5 on 2020-05-03 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date Published'),
        ),
    ]
