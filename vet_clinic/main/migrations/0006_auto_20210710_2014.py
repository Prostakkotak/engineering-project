# Generated by Django 3.0.1 on 2021-07-10 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210710_2010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phone',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='doctorreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 20, 14, 9, 174229)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 20, 14, 9, 173233)),
        ),
        migrations.AlterField(
            model_name='servicereview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 20, 14, 9, 174229)),
        ),
    ]
