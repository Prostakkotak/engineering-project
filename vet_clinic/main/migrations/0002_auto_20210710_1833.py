# Generated by Django 3.0.1 on 2021-07-10 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default='Описание', help_text='Описание услуги'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 18, 33, 28, 438663)),
        ),
    ]
