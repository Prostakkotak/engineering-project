# Generated by Django 3.0.1 on 2021-07-10 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Иван Иванов Иванович', help_text='ФИО Врача', max_length=100)),
                ('position', models.CharField(default='Практикант', help_text='Должность', max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('bio', models.TextField(blank=True, help_text='Краткая информация о враче')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Текст отзыва')),
                ('author', models.CharField(help_text='Имя автора отзыва', max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 7, 10, 14, 35, 57, 954898), editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Анестезия', help_text='Название услуги', max_length=100)),
                ('price', models.PositiveIntegerField(default=1000, help_text='Цена услуги')),
                ('category', models.CharField(choices=[('Анестезия', 'Анестезия'), ('Диагностика', 'Диагностика'), ('Онкология', 'Онкология'), ('ОРИТ', 'ОРИТ'), ('Офтальмология', 'Офтальмология'), ('Процедуры', 'Процедуры'), ('Стационар', 'Стационар'), ('Стерилизация', 'Стерилизация'), ('Стоматология', 'Стоматология'), ('Терапия', 'Терапия'), ('Хирургия', 'Хирургия'), ('Экзотолог', 'Экзотолог')], default='другое', max_length=50)),
            ],
        ),
    ]
