<<<<<<< HEAD
from django.shortcuts import render
from .serializers import ChangePasswordSerializer, UserLoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(email = email ,password = password )
        if user is not None:
            tokens = get_tokens_for_user(user)
            return Response({'msg':'The user is sucessfully logged in','tokens ':tokens},status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = IsAuthenticated
    def post(self,request,format=None):
        serializer = ChangePasswordSerializer(data=request.data,context={'request':request}) 
        serializer.is_valid(raise_exception=True)
        request.user.set_password = serializer.validated_data.get('confrim_password')
        request.user.save()
        return Response('The password has been changed sucessfully')


            
=======
import email
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from rest_framework.response import Response
from rest_framework import (
    status, 
    )
from rest_framework.views import APIView

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        userid = user.id
        user_role = user.user_role
        password = user.check_password(password)
        if not user:
            return Response('The provided email is incorrect')
        if not password:
            return Response('The provided password is incorrect')
       
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'email': email,
            'token': token,
            'user_id': userid,
            'userrole': user_role,
        }
        return response

class TeacherAPIView(ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()

    def post(self, request):
        if self.request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = request.data.get("email")
            if User.objects.filter(username=email, email=email).exists():
                return Response({"Message":"Already Exists"}, status=status.HTTP_404_NOT_FOUND)
            else:
                user = User.objects.create(username=email, email=email)
                user.set_password(request.data.get("password"))
                user.user_role = 'teacher'
                user.save()
                Teacher.objects.create(user=user, full_name=request.data.get("full_name"), contact=request.data.get("contact"))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message":"You are not Super User!!"}, status=status.HTTP_403_FORBIDDEN)
>>>>>>> d8e3709d4a693f5096bdb0771b7024288584a0a2
