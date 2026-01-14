from rest_framework import serializers
from . models import Profile
from django.contrib.auth.models import User
from .utils import SendMail

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializers
        fields = ["fullname", "phone", "gender", "profile_pix"]


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model=Profile
        fields = ["fullname", "username", "email", "password1", "password2", "gender", "phone", "profile_pix"]



    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already exists")
        return value       

    def validate(self, data):
        if data ['password1'] != data ['password2']:
            raise serializers.ValidationError("password not match")
            # if data['email'].exists():
            #     raise serializers.ValidationError("email already exists")
        return data 
        
    def create (self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password1')

        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(
            user=user,
            fullname = validated_data['fullname'],
            # username = validated_data['username'],
            gender= validated_data['gender'],
            phone= validated_data['phone'],
            profile_pix= validated_data['profile_pix'],
        )

        SendMail(email)

        return profile