from django.urls import path
from .views import *

urlpatterns = [
    path('books/',CreateandGetBooks.as_view()),
    path('class/',CreateandGetClass.as_view()),
    path('update_class/<int:pk>',UpdateClass.as_view()),
    path('fee_notifications/',CreateandGetFeeNotification.as_view()),
    path('update_fee_notifications/',UpdateFeeNotification.as_view()),
    path('event_notifications/',CreateandGetEventNotification.as_view()),
    path('update_event_notifications/',UpdateEventNotification.as_view()),
    path('create_settings/',CreateSettingLimitView.as_view()),
    path('create_settings/<int:pk>/',UpdateSettingLimitView.as_view()),
    path('create_feedback/',CreateFeedbackView.as_view()),
    path('get_feedback/',GetFeedBackView.as_view()),
    path('update_feedback/',UpdateFeedBack.as_view()),
    path('about_admin/',CreateAboutAmdinView.as_view())
]