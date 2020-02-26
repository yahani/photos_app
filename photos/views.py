from django.utils.datetime_safe import datetime
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import get_object_or_404, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Photo


class PhotosView(APIView):

    def put(self, request):
        if 'image' not in request.data:
            raise ParseError("Invalid request")

        data = request.data
        data['user_id'] = request.user.id
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, photo_id):
        db_photo = get_object_or_404(Photo.objects.all(), pk=photo_id)

        enable_edit = request.user == db_photo.user_id
        if enable_edit is False:
            return Response(status=status.HTTP_403_FORBIDDEN)

        data = request.data

        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, photo_id):
        photo = get_object_or_404(Photo.objects.all(), pk=photo_id)
        photo.delete()
        return Response({"message": "Photo ID `{}` is deleted.".format(photo_id)}, status=status.HTTP_200_OK)


class PhotosViewSet(ModelViewSet):

    queryset = Photo.objects.all()
    template_name = 'list.html'

    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        data = request.data
        sort_publish_datetime_asc = data['sort_publish_datetime'] if 'sort_publish_datetime' in data else 'desc'
        sort_type = 'publish_datetime' if sort_publish_datetime_asc == 'asc' else '-publish_datetime'

        queryset = self.filter_queryset(self.get_queryset())

        queryset = queryset.order_by(sort_type)

        return Response(data, status=status.HTTP_200_OK)