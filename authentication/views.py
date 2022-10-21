from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView
from .permissions import *

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
        else:
            return Response({'msg':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = ChangePasswordSerializer(data=request.data,context={'request':request}) 
        serializer.is_valid(raise_exception=True)
        request.user.set_password = serializer.validated_data.get('confirm_password')
        request.user.save()
        return Response('The password has been changed sucessfully')

class LogOutView(APIView):
    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)

    
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Student.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Teacher.objects.all()