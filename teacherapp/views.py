from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from .models import Assignment, Attendence, Notes, Message
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import *
from django.db.models import Q


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


class SubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        qs = Subject.objects.filter(created_by__user=self.request.user)
        user_data = self.request.GET.get('user_data')
        if user_data is not None:
            qs = qs.filter(
                (Q(subject_name__icontains=user_data)) |
                (Q(subject__year=user_data))
            ).distinct()
        return qs

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.user_role == 'teacher':
            qs = Message.objects.filter(created_by__user=self.request.user)
        else:
            qs = Message.objects.all()
        user_data = self.request.GET.get('user_data')
        if user_data is not None:
            qs = qs.filter(
                (Q(message__icontains=user_data)) |
                (Q(subject__year=user_data))
            ).distinct()
        return qs

class AssignmentListView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.user_role == 'teacher':
            qs = Assignment.objects.filter(created_by__user=self.request.user)
        else:
            qs = Assignment.objects.all()
        user_data = self.request.GET.get('user_data')
        if user_data is not None:
            qs = qs.filter(
                (Q(title__icontains=user_data)) |
                (Q(assigned_date__icontains=user_data)) |
                (Q(deadline_date__icontains=user_data)) |
                (Q(status__icontains=user_data)) |
                (Q(subject__year=user_data))
            ).distinct()
        return qs

class NotesListView(generics.ListAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.user_role == 'teacher':
            qs = Notes.objects.filter(created_by__user=self.request.user)
        else:
            qs = Notes.objects.all()
        user_data = self.request.GET.get('user_data')
        if user_data is not None:
            qs = qs.filter(
                (Q(title__icontains=user_data)) |
                (Q(subject__year=user_data))
            ).distinct()
        return qs

class AttendenceListView(generics.ListAPIView):
    serializer_class = AttendenceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.user_role == 'teacher':
            qs = Attendence.objects.filter(attended_by__user=self.request.user)
        else:
            qs = Attendence.objects.filter(student__user=self.request.user)
        user_data = self.request.GET.get('user_data')
        if user_data is not None:
            qs = qs.filter(
                (Q(status__icontains=user_data)) |
                (Q(subject__subject_name=user_data)) |
                (Q(student__id=user_data)) |
                (Q(student__full_name=user_data)) |
                (Q(student__registration_number=user_data)) |
                (Q(student__batch_name=user_data)) |
                (Q(student__contact=user_data))
            ).distinct()
        return qs

# Create your views here.
