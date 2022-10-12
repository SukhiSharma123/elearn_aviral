from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('teacher/', TeacherAPIView.as_view(), name='teacher'),
]