from django.contrib import admin
from .models import Student, Teacher, User

admin.site.register([User,Teacher,Student])

# Register your models here.
