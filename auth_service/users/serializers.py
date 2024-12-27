# user/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'is_first_category', 'is_second_category', 'is_third_category', 'is_fourth_category']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_first_category=validated_data.get('is_first_category', False),
            is_second_category=validated_data.get('is_second_category', False),
            is_third_category=validated_data.get('is_third_category', False),
            is_fourth_category=validated_data.get('is_fourth_category', False),
        )
        return user
