from rest_framework.serializers import ModelSerializer

from .models import *

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class DoctorReviewSerializer(ModelSerializer):
    class Meta:
        model = DoctorReview
        fields = "__all__"

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ServiceReviewSerializer(ModelSerializer):
    class Meta:
        model = ServiceReview
        fields = "__all__"

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
