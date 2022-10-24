
from email.policy import default
from random import choices
from django.db import models

from authentication.models import Student, Teacher
from elearn.models import Class

attendence = (
    ('absent','absent'),
    ('present','present'),
)
submitted = (
    ('submitted','submitted'),
    ('not submitted','not submitted'),
)

# Create your models here.
class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_attendence')
    subject = models.ForeignKey(Class, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=attendence, blank=True, null=True)
    attended_on = models.DateTimeField(auto_now_add=True)
    attended_by = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True)

class Message(models.Model):
    message = models.CharField(max_length=255)
    subject = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Class, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    deadline_date = models.DateField()
    status = models.CharField(max_length=255, choices=submitted, blank=True, null=True)
    file = models.FileField(upload_to='file/', blank=True, null=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Notes(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='note/')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)


