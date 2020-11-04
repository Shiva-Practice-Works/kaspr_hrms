# Generated by Django 2.2.14 on 2020-11-03 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0003_auto_20201103_1124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Band_Status',
        ),
        migrations.AddField(
            model_name='conversion_box',
            name='status',
            field=models.CharField(default=datetime.datetime(2020, 11, 3, 11, 34, 31, 793743, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
