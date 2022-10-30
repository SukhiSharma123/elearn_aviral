from django.urls import path, include 
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('attendence', AttendenceViewSet, basename='attendence')
router.register('message', MessageViewSet, basename='message')
router.register('assignment', AssignmentViewSet, basename='assignment')
router.register('notes', NotesViewSet, basename='notes')
router.register('subject', SubjectViewSet, basename='subject')

urlpatterns = [
    path('', include(router.urls)),
    path('subject-list/', SubjectListView.as_view(), name='subject-list'),
    path('message-list/', MessageListView.as_view(), name='message-list'),
    path('assignment-list/', AssignmentListView.as_view(), name='assignment-list'),
    path('notes-list/', NotesListView.as_view(), name='notes-list'),
    path('attendence-list/', AttendenceListView.as_view(), name='attendence-list'),
]