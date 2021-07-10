from os import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('services/', views.Services.as_view(), name='services'),
    path('services/<pk>/', views.ServicesItem.as_view(), name="services-item"),
    path('doctors/', views.Doctors.as_view(), name="doctors"),
    path('doctors/<pk>/', views.DoctorsItem.as_view(), name="doctors-item"),
]