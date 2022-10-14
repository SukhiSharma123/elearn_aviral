from rest_framework import serializers
from .models import *

class CreateandListBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def validate(self,attrs):
        if Settings.objects.all().first().number_of_books_boolean:
            if Books.objects.count()==400:
                raise serializers.ValidationError('More Books cannot be added cause there is limitation in settings')
        return attrs


class CreateandShowFeeNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeNotification
        fields = '__all__'

class CreateandShowClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class 
        fields = '__all__'

    def validate(self,attrs):
        if Settings.objects.all().first().number_of_books_boolean:
            if Class.objects.count()==20:
                raise serializers.ValidationError('More classes cannot be added cause there is limitation in settings')
        return attrs


class CreateandShowEventNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventNotification
        fields = '__all__'

class CreateBooleanLimitSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'