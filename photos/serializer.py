from rest_framework import serializers
from .models import Photo
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def update(self, instance, data):
        instance.caption = data.get('caption', instance.caption)
        instance.saved = data.get('saved', instance.saved)

        instance.save()
        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)