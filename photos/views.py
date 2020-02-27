from django.utils.datetime_safe import datetime
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import get_object_or_404, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Photo
from .serializer import PhotoSerializer


class PhotosView(APIView):

    def put(self, request):
        if 'image' not in request.data:
            raise ParseError("Invalid request")

        data = request.data
        _mutable = data._mutable
        data._mutable = True
        data['user'] = request.user.id

        if 'draft' not in request.data or request.data['draft'] is False:
            data['created'] = datetime.now()

        data._mutable = _mutable
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, photo_id):
        db_photo = get_object_or_404(Photo.objects.all(), pk=photo_id)

        data = request.data
        _mutable = data._mutable
        data._mutable = True
        if 'draft' not in request.data or request.data['draft'] is False:
            data['created'] = datetime.now()
        data._mutable = _mutable
        serializer = PhotoSerializer(instance=db_photo, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, photo_id):
        photo = get_object_or_404(Photo.objects.all(), pk=photo_id)
        photo.delete()
        return Response({"message": "Photo ID `{}` is deleted.".format(photo_id)}, status=status.HTTP_200_OK)


class PhotosViewSet(ModelViewSet):
    queryset = Photo.objects.all()

    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        data = request.data
        sort = data['sort'] if 'sort' in data else 'desc'
        sort_type = 'created' if sort else '-created'

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.order_by(sort_type)
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
