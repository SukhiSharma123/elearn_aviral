from rest_framework import serializers
from django.contrib.auth import get_user_model 
User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['email','password']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=20)
    new_password = serializers.CharField(max_length=20)
    confirm_password = serializers.CharField(max_length=20)

    class Meta():
        fields = '__all__'

    def validate(self,attrs):
        if attrs.get('new_password') != attrs.get('confrim_password'):
            raise serializers.ValidationError('The new password and confrim password does not match')

        user = self.context.get('request').user
        if not user.check_password(attrs.get('old_password')):
            raise serializers.ValidationError('The old password is not correct so you cannot change the password')
        