# Generated by Django 3.2.7 on 2022-06-05 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220604_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 6, 0, 8, 56, 870651)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 6, 0, 8, 56, 870651)),
        ),
        migrations.AlterField(
            model_name='servicereview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 6, 0, 8, 56, 870651)),
        ),
    ]
