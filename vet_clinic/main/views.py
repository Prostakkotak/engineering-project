from typing import ContextManager
from django.shortcuts import render
from django.views.generic import View
from .models import *


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