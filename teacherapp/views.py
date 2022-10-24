from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Assignment, Attendence, Notes, Message
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import *


class AttendenceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendenceSerializer
    permission_classes = [IsTeacherOrReadOnly]
    queryset = Attendence.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsMessageOrReadOnly]
    queryset = Message.objects.all()

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [IsMessageOrReadOnly]
    queryset = Assignment.objects.all()

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    permission_classes = [IsMessageOrReadOnly]
    queryset = Notes.objects.all()


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [IsMessageOrReadOnly]
    queryset = Subject.objects.all()

# Create your views here.
