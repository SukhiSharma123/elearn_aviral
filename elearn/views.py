from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *


class CreateandGetClass(ListCreateAPIView):
    serializer_class = CreateandShowClassSerializer
    queryset = Class.objects.all()

class CreateandGetBooks(ListCreateAPIView):
    serializer_class = CreateandListBooksSerializer
    queryset = Books.objects.all()

class CreateandGetEventNotification(ListCreateAPIView):
    serializer_class = CreateandShowEventNotificationSerializer
    queryset = EventNotification.objects.all()


class CreateandGetFeeNotification(ListCreateAPIView):
    serializer_class = CreateandShowFeeNotificationSerializer
    queryset = FeeNotification.objects.all()

    



