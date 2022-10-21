from django.urls import path, include 
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('attendence', AttendenceViewSet, basename='attendence')
router.register('message', MessageViewSet, basename='message')
router.register('assignment', AssignmentViewSet, basename='assignment')
router.register('notes', NotesViewSet, basename='notes')

urlpatterns = [
    path('', include(router.urls)),
]