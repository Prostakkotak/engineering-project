from wsgiref.validate import validator
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import *

def not_short(value):
    if len(value) < 5:
        raise serializers.ValidationError('This field is too short')

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class NewDoctorSerializer(Serializer):
    name = serializers.CharField(validators=[not_short])
    position = serializers.CharField(validators=[not_short])
    bio = serializers.CharField(validators=[not_short])

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
