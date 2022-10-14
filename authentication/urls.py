<<<<<<< HEAD
from django.urls import path 
from .views import *

urlpatterns = [
    path('login_user', UserLoginView.as_view(),name='login_user'),
    path('change_password/',ChangePasswordView.as_view(),name='change_password')
=======
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('teacher/', TeacherAPIView.as_view(), name='teacher'),
>>>>>>> d8e3709d4a693f5096bdb0771b7024288584a0a2
]