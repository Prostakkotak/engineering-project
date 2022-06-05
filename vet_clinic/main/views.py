from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from .models import *


# DRF
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Filters
import django_filters.rest_framework
from rest_framework import filters


class Index(View):
    def get(self, request):

        doctors = Doctor.objects.all()
        reviews = Review.objects.all()
        services = Service.objects.all()

        return render(request, 'index.html', context={
            'services': services,
            'reviews': reviews,
            'doctors': doctors,
        })


class Contacts(View):
    def get(self, request):

        contacts = Contact.objects.all()

        return render(request, 'contacts.html', context={
            'contacts': contacts,
        })


class Services(View):
    def get(self, request):

        searchOption = request.GET.get('q')

        if (searchOption is not None):
            if (request.GET.get('cat') == ''):
                services = Service.objects.filter(
                    name__icontains=request.GET.get('q'))
            else:
                services = Service.objects.filter(
                    name__icontains=request.GET.get('q'), category=request.GET.get('cat'))
        else:
            services = Service.objects.all()

        return render(request, 'services.html', context={
            'services': services,
        })


class ServicesItem(View):
    def get(self, request, pk):
        item = Service.objects.get(pk=pk)

        reviews = ServiceReview.objects.filter(service=pk)

        return render(request, 'services-item.html', context={
            'item': item,
            "reviews": reviews,
        })


class Doctors(View):
    def get(self, request):

        searchOption = request.GET.get('q')

        if (searchOption is not None):
            doctors = Doctor.objects.filter(
                name__icontains=request.GET.get('q'))
        else:
            doctors = Doctor.objects.all()

        return render(request, 'doctors.html', context={
            'doctors': doctors,
        })


class DoctorsItem(View):
    def get(self, request, pk):
        item = Doctor.objects.get(pk=pk)

        reviews = DoctorReview.objects.filter(doctor=pk)

        return render(request, 'doctors-item.html', context={
            "item": item,
            "reviews": reviews,
        })


""" API Views """

class DoctorsViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'position']

class DoctorReviewsViewSet(ModelViewSet):
    serializer_class = DoctorReviewSerializer
    queryset = DoctorReview.objects.all()

    def get_queryset(self): # Переписываем станданртый метод чтобы брать отзывы по переданному id
        doctor_id = self.request.query_params.get('id')
        queryset = DoctorReview.objects.filter(Q(doctor=doctor_id))

        return queryset

class ServicesViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'category']
 
class ServiceReviewsViewSet(ModelViewSet):
    serializer_class = ServiceReviewSerializer
    queryset = ServiceReview.objects.all()

    def get_queryset(self): # Переписываем станданртый метод чтобы брать отзывы по переданному id
        service_id = self.request.query_params.get('id')
        queryset = ServiceReview.objects.filter(service=service_id)

        return queryset