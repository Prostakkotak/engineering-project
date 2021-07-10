# Generated by Django 3.0.1 on 2021-07-10 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210710_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='Телефон для связи с клиникой', max_length=15)),
                ('name', models.CharField(help_text="Название, т.е. например 'Горячая линия' и тд", max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='doctorreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 20, 10, 21, 930710)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 20, 10, 21, 930710)),
        ),
        migrations.AlterField(
            model_name='servicereview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 20, 10, 21, 931710)),
        ),
    ]
