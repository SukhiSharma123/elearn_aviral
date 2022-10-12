from rest_framework import serializers
from .models import *


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email']
        extra_kwargs = {'password': {'write_only': True}}

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    email = serializers.EmailField()
    full_name = serializers.CharField()
    contact = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Teacher
        fields = ['email','full_name','contact','password','user']
        extra_kwargs = {'password': {'write_only': True}}

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    email = serializers.EmailField()
    full_name = serializers.CharField()
    registration_number = serializers.CharField()
    batch_name = serializers.CharField()
    contact = serializers.CharField()
    dob = serializers.DateField()

    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}