import email
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


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=20)
    class Meta():
        model = User
        fields = ['email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    full_name = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = Teacher
        fields = '__all__'
    
    def create(self, validated_data):
        user = validated_data.pop('user')
        if User.objects.filter(email=user['email']).exists():
            raise serializers.ValidationError('User Exists')
        else:
            teacher_user = User.objects.create(username=user['email'], email=user['email'])
            teacher_user.set_password(user['password'])
            teacher_user.user_role = 'teacher'
            teacher_user.save()
            student = Teacher.objects.create(
                user=teacher_user, 
                full_name = validated_data['full_name'], 
                contact=validated_data['contact'],
                )
            return student
    
    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        if User.objects.filter(email=user['email']).exists():
            raise serializers.ValidationError('User Exists')
        else:
            if user['email'] is not None:
                student_user = User.objects.get(email=instance.user.email)
                student_user.email = user['email']
                student_user.username = user['email']
                student_user.save()
                instance.user = student_user
                instance.full_name = validated_data.get('full_name', instance.full_name)
                instance.contact = validated_data.get('contact', instance.contact)
                instance.save()
            else:
                instance.full_name = validated_data.get('full_name', instance.full_name)
                instance.contact = validated_data.get('contact', instance.contact)
                instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    full_name = serializers.CharField()
    registration_number = serializers.CharField()
    batch_name = serializers.CharField()
    contact = serializers.CharField()
    dob = serializers.DateField()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('user')
        if User.objects.filter(email=user['email']).exists():
            raise serializers.ValidationError('User Exists')
        else:
            student_user = User.objects.create(username=user['email'], email=user['email'])
            student_user.set_password(user['password'])
            student_user.user_role = 'student'
            student_user.save()
            student = Student.objects.create(
                user=student_user, 
                full_name = validated_data['full_name'], 
                registration_number=validated_data['registration_number'],
                batch_name=validated_data['batch_name'],
                contact=validated_data['contact'],
                dob=validated_data['dob'],
                )
            return student
    
    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        if User.objects.filter(email=user['email']).exists():
            raise serializers.ValidationError('User Exists')
        else:
            if user['email'] is not None:
                student_user = User.objects.get(email=instance.user.email)
                student_user.email = user['email']
                student_user.username = user['email']
                student_user.save()
                instance.user = student_user
                instance.full_name = validated_data.get('full_name', instance.full_name)
                instance.registration_number = validated_data.get('registration_number', instance.registration_number)
                instance.batch_name = validated_data.get('batch_name', instance.batch_name)
                instance.contact = validated_data.get('contact', instance.contact)
                instance.dob = validated_data.get('dob', instance.dob)
                instance.save()
            else:
                instance.full_name = validated_data.get('full_name', instance.full_name)
                instance.registration_number = validated_data.get('registration_number', instance.registration_number)
                instance.batch_name = validated_data.get('batch_name', instance.batch_name)
                instance.contact = validated_data.get('contact', instance.contact)
                instance.dob = validated_data.get('dob', instance.dob)
                instance.save()
        return instance

