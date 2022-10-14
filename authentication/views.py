from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView

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