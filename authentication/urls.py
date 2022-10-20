from django.urls import path 
from .views import *

urlpatterns = [
    path('login_user/', UserLoginView.as_view(),name='login_user'),
    path('change_password/',ChangePasswordView.as_view(),name='change_password'),
    path('logoout/',LogOutView.as_view(),name='logout'),
    path('teacher/', TeacherAPIView.as_view(), name='teacher'),
    path('student/', StudentAPIView.as_view(), name='student'),
]