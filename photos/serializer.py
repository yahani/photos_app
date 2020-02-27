from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def update(self, instance, data):
        instance.caption = data.get('caption', instance.caption)
        instance.created = data.get('created', instance.created)

        instance.save()
        return instance