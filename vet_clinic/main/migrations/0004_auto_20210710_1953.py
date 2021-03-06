# Generated by Django 3.0.1 on 2021-07-10 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210710_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 19, 53, 8, 599356)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 19, 53, 8, 598356)),
        ),
        migrations.CreateModel(
            name='ServiceReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='Отзыв')),
                ('author', models.CharField(default='Иван Иванов', help_text='Автор отзыва', max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 7, 10, 19, 53, 8, 599356))),
                ('service', models.ForeignKey(help_text='Какой услуге отзыв', on_delete=django.db.models.deletion.CASCADE, to='main.Doctor')),
            ],
        ),
    ]
