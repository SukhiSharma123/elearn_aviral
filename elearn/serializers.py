from rest_framework import serializers
from .models import *

class CreateandListBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class CreateandShowFeeNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeNotification
        fields = '__all__'

class CreateandShowClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class 
        fields = '__all__'

class CreateandShowEventNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventNotification
        fields = '__all__'
