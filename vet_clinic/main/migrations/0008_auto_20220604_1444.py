# Generated by Django 3.2.9 on 2022-06-04 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220528_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 14, 44, 38, 181176)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 14, 44, 38, 181176)),
        ),
        migrations.AlterField(
            model_name='servicereview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 14, 44, 38, 181176)),
        ),
    ]
