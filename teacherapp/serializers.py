from turtle import title
from rest_framework import serializers
from .models import Attendence, Assignment, Message, Notes
from django.contrib.auth import get_user_model 
User = get_user_model()
from authentication.models import Student, Teacher
from elearn.models import Class

class StudentViewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    user = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    registration_number = serializers.CharField(required=False)
    batch_name = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    dob= serializers.CharField(required=False)
    class Meta:
        model = Student
        fields = '__all__'

class TeacherViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectViewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    faculty = serializers.CharField(required=False)
    year= serializers.CharField(required=False)
    class Meta:
        model = Class
        fields = '__all__'

class AttendenceSerializer(serializers.ModelSerializer):
    student = StudentViewSerializer()
    subject = SubjectViewSerializer()
    status = serializers.CharField()
    attended_on= serializers.CharField(required=False)
    attended_by = TeacherViewSerializer(required=False)
    

    class Meta:
        model = Attendence
        fields = '__all__'
    
    def create(self, validated_data):
        student = validated_data.pop('student')
        subject = validated_data.pop('subject')
        if Student.objects.filter(id=student['id']).exists():
            student_detail = Student.objects.get(id=student['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        if Class.objects.filter(id=subject['id']).exists():
            class_detail = Class.objects.get(id=subject['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        if Teacher.objects.filter(user=User.objects.get(username=self.context['request'].user.username)).exists():
            attendence = Attendence.objects.create(
                student=student_detail, 
                subject=class_detail, 
                status = validated_data['status'], 
                attended_by = Teacher.objects.get(user=User.objects.get(username=self.context['request'].user.username)),
                )
            return attendence
        else:
            raise serializers.ValidationError('Your Teacher Account has been deleted')
    
    def update(self, instance, validated_data):
        student = validated_data.pop('student')
        subject = validated_data.pop('subject')
        if Student.objects.filter(id=student['id']).exists():
            student_detail = Student.objects.get(id=student['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        if Class.objects.filter(id=subject['id']).exists():
            class_detail = Class.objects.get(id=subject['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        instance.student = student_detail
        instance.subject = class_detail
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class MessageSerializer(serializers.ModelSerializer):
    subject = SubjectViewSerializer()
    message = serializers.CharField()
    created_on= serializers.CharField(required=False)
    created_by = TeacherViewSerializer(required=False)
    

    class Meta:
        model = Message
        fields = '__all__'
    
    def create(self, validated_data):
        subject = validated_data.pop('subject')
        if Class.objects.filter(id=subject['id']).exists():
            class_detail = Class.objects.get(id=subject['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        if Teacher.objects.filter(user=User.objects.get(username=self.context['request'].user.username)).exists():
            message = Message.objects.create(
                subject=class_detail, 
                message = validated_data['message'], 
                created_by = Teacher.objects.get(user=User.objects.get(username=self.context['request'].user.username)),
                )
            return message
        else:
            raise serializers.ValidationError('Your Teacher Account has been deleted')
    
    def update(self, instance, validated_data):
        subject = validated_data.pop('subject')
        if Class.objects.filter(id=subject['id']).exists():
            class_detail = Class.objects.get(id=subject['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        instance.subject = class_detail
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance


class AssignmentSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    subject = SubjectViewSerializer()
    assigned_date = serializers.DateField()
    deadline_date = serializers.DateField()
    status= serializers.CharField(required=False)
    file = serializers.FileField(required=False)
    created_by = TeacherViewSerializer(required=False)
    

    class Meta:
        model = Assignment
        fields = '__all__'
    
    def create(self, validated_data):
        subject = validated_data.pop('subject')
        if Class.objects.filter(id=subject['id']).exists():
            class_detail = Class.objects.get(id=subject['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        if Teacher.objects.filter(user=User.objects.get(username=self.context['request'].user.username)).exists():
            assignment = Assignment.objects.create(
                subject=class_detail,
                created_by = Teacher.objects.get(user=User.objects.get(username=self.context['request'].user.username)),
                **validated_data
                )
            return assignment
        else:
            raise serializers.ValidationError('Your Teacher Account has been deleted')
    
    def update(self, instance, validated_data):
        subject = validated_data.pop('subject')
        if Class.objects.filter(id=subject['id']).exists():
            class_detail = Class.objects.get(id=subject['id'])
        else:
            raise serializers.ValidationError('Not Exists')
        instance.subject = class_detail
        instance.title = validated_data.get('title', instance.title)
        instance.assigned_date = validated_data.get('assigned_date', instance.assigned_date)
        instance.deadline_date = validated_data.get('deadline_date', instance.deadline_date)
        instance.status = validated_data.get('status', instance.status)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance

class NotesSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    file = serializers.FileField(required=False)
    created_on = serializers.CharField(required=False)
    created_by = TeacherViewSerializer(required=False)
    

    class Meta:
        model = Notes
        fields = '__all__'
    
    def create(self, validated_data):
        if Teacher.objects.filter(user=User.objects.get(username=self.context['request'].user.username)).exists():
            note = Notes.objects.create(
                created_by = Teacher.objects.get(user=User.objects.get(username=self.context['request'].user.username)),
                **validated_data
                )
            return note
        else:
            raise serializers.ValidationError('Your Teacher Account has been deleted')
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance