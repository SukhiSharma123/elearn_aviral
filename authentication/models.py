from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            email=email,
            is_staff = True, 
            username=email,
            is_superuser = True, 
            user_role = 'superuser',
        )
        user.set_password(password)
        user.save()
       
        
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


USER_ROLE = (
    ("user","user"),
    ("vendor","vendor"),
    ("superuser","superuser"),
    ("developer","developer"),
    ("teacher","teacher"),
    ("student","student"),
    )

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_role = models.CharField(max_length=50, default="student", choices=USER_ROLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return str(self.email)

from django.contrib.auth import get_user_model
User = get_user_model()
 

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return str(self.full_name)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    full_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    batch_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    dob = models.DateField()

    def __Str__(self):
        return str(self.full_name)