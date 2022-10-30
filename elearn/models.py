from xml.dom import VALIDATION_ERR, ValidationErr
from django.db import models

# Create your models here.
from random import choices
from django.db import models

#Admin Model 

faculty = (
    ('testing','Testing'),
    ('testing2','Testing2'),
    ('testing3','Testing3')



)

year = (
    ('2078','78'),
    ('2077','77'),
    ('2076','76')
)

class Class(models.Model):
    faculty = models.CharField(max_length=20,choices=faculty)
    year = models.CharField(max_length=10,choices=year)

    # def clean(self):
    #     if Settings.objects.all().first().number_of_batches_boolean:
    #         if Class.objects.count()==1:
    #             raise VALIDATION_ERR('More classes cannot be added cause there is limitation in settings')
    #     return super(Class,self).clean()

    def __str__(self):
        return self.faculty
class Books(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=20,choices=year)
    code_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class FeeNotification(models.Model):
    batch_name= models.CharField(max_length=10,choices=faculty)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message


class EventNotification(models.Model):
    batch_name = models.CharField(max_length=20,choices = faculty)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message

class Settings(models.Model):
    number_of_batches_boolean = models.BooleanField()
    number_of_books_boolean = models.BooleanField()
    number_of_teachers_boolean = models.BooleanField()




class FeedBack(models.Model):
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class AboutAdmin(models.Model):
    about = models.CharField(max_length=200)


    def __str__(self):
        return self.about 

