from django.urls import path, include 
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('student', StudentViewSet, basename='student')
router.register('teacher', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('login_user/', UserLoginView.as_view(),name='login_user'),
    path('change_password/',ChangePasswordView.as_view(),name='change_password'),
    path('logoout/',LogOutView.as_view(),name='logout'),
    path('delete_user/<int:pk>/',DeleteUserView.as_view()),
    path('', include(router.urls)),
    path('student-list/',StudentListView.as_view(),name='student-list'),
]