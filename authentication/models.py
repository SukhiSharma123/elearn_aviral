from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email,phonenumber,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phonenumber=phonenumber
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phonenumber,username,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            email=email,
            phonenumber=phonenumber,
            is_staff = True, 
            username=username,
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
    ('developer',"developer")
    )

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profilepicture = models.ImageField(upload_to='profilepicture/' ,blank=True, null=True)
    # new_phone = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    # new_email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    # otp = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_role = models.CharField(max_length=50, default="user", choices=USER_ROLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phonenumber','username']
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return str(self.email)

    