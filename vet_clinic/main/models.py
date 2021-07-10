from django import http
from django.db import models
from django.db.models.fields import CharField, DateTimeField
from datetime import date, datetime

class Doctor(models.Model):
    name = models.CharField(max_length=100, help_text='ФИО Врача', default='Иван Иванов Иванович')
    position = models.CharField(max_length=100, help_text='Должность', default='Практикант')
    photo = models.ImageField()
    bio = models.TextField(blank=True, help_text="Краткая информация о враче")

    def __str__(self) -> str:
        return self.name + ', ' + self.position

class Service(models.Model):
    name = models.CharField(max_length=100, help_text='Название услуги', default='Анестезия')
    price = models.PositiveIntegerField(help_text='Цена услуги', default=1000)

    CATEGORIES = (
        ('Анестезия', 'Анестезия'),
        ('Диагностика', 'Диагностика'),
        ('Онкология', 'Онкология'),
        ('ОРИТ', 'ОРИТ'),
        ('Офтальмология', 'Офтальмология'),
        ('Процедуры', 'Процедуры'),
        ('Стационар', 'Стационар'),
        ('Стерилизация', 'Стерилизация'),
        ('Стоматология', 'Стоматология'),
        ('Терапия', 'Терапия'),
        ('Хирургия', 'Хирургия'),
        ('Экзотолог', 'Экзотолог')
    )

    category = models.CharField(max_length=50, default='другое', choices=CATEGORIES)
    description = models.TextField(help_text='Описание услуги', default='Описание')

    def __str__(self) -> str:
        return self.name + ', ' + str(self.price) + 'р , ' + self.category

class Review(models.Model):
    content = models.TextField(help_text="Текст отзыва")
    author = models.CharField(max_length=100, help_text="Имя автора отзыва")
    date = models.DateTimeField(default=datetime.now(), editable=True)

    def __str__(self) -> str:
        return self.author 


class DoctorReview(models.Model):
    content = models.TextField(default='Отзыв')
    author = models.CharField(max_length=100, help_text="Автор отзыва", default='Иван Иванов')
    date = models.DateTimeField(default=datetime.now(), editable=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, help_text='Какому врачу отзыв')

    def __str__(self) -> str:
        return self.author


class ServiceReview(models.Model):
    content = models.TextField(default='Отзыв')
    author = models.CharField(max_length=100, help_text="Автор отзыва", default='Иван Иванов')
    date = models.DateTimeField(default=datetime.now(), editable=True)
    service = models.ForeignKey(Doctor, on_delete=models.CASCADE, help_text='Какой услуге отзыв')

    def __str__(self) -> str:
        return self.author


class Contact(models.Model):
    value = CharField(max_length=100, help_text="Телефон для связи с клиникой")
    name = CharField(max_length=50, help_text="Название, т.е. например 'Горячая линия' и тд")

    def __str__(self) -> str:
        return self.name + ": " + self.value