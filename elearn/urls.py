from django.urls import path
from .views import *

urlpatterns = [
    path('books/',CreateandGetBooks.as_view()),
    path('class/',CreateandGetClass.as_view()),
    path('fee_notifications/',CreateandGetFeeNotification.as_view()),
    path('event_notifications/',CreateandGetEventNotification.as_view())
]