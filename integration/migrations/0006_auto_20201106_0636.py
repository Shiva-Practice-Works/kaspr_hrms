# Generated by Django 2.2.14 on 2020-11-06 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0005_auto_20201105_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion_box',
            name='Hrrounwillbe',
            field=models.DateField(default=datetime.datetime(2020, 11, 6, 6, 36, 52, 971899)),
        ),
        migrations.AlterField(
            model_name='conversion_box',
            name='hr_msg',
            field=models.CharField(default='No Data', max_length=500),
        ),
        migrations.AlterField(
            model_name='conversion_box',
            name='hrround',
            field=models.CharField(default='No Data', max_length=180),
        ),
    ]
