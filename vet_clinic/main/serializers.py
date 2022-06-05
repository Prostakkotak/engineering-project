from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import *

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class NewDoctorSerializer(Serializer):
    name = serializers.CharField()
    position = serializers.CharField()
    bio = serializers.CharField()

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
