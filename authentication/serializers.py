from rest_framework import serializers
from django.contrib.auth import get_user_model 
User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=20)
    class Meta():
        fields = ['email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=20)
    new_password = serializers.CharField(max_length=20)
    confirm_password = serializers.CharField(max_length=20)

    class Meta():
        fields = '__all__'

    def validate(self,attrs):
        if attrs.get('new_password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('The new password and confrim password does not match')

        user = self.context.get('request').user
        if not user.check_password(attrs.get('old_password')):
            raise serializers.ValidationError('The old password is not correct so you cannot change the password')

        return attrs
        
from .models import *


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email']
        extra_kwargs = {'password': {'write_only': True}}

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.EmailField()
    full_name = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(required=False)
    user = serializers.EmailField()
    full_name = serializers.CharField()
    registration_number = serializers.CharField()
    batch_name = serializers.CharField()
    contact = serializers.CharField()
    dob = serializers.DateField()

    class Meta:
        model = Student
        fields = '__all__'
