from django.utils.datetime_safe import datetime
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.generics import get_object_or_404, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Photo
from .serializer import PhotoSerializer
from .serializer import RegistrationSerializer


class PhotosView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        if 'image' not in request.data:
            raise ParseError("Invalid request")

        data = request.data
        _mutable = data._mutable
        data._mutable = True
        data['user'] = request.user.id

        if 'is_draft' not in request.data or request.data['is_draft'] is False:
            data['saved'] = datetime.now()

        data._mutable = _mutable
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, photo_id):
        db_photo = get_object_or_404(Photo.objects.all(), pk=photo_id)

        is_authorized = request.user == db_photo.user
        if is_authorized is False:
            return Response(status=status.HTTP_403_FORBIDDEN)

        data = request.data
        _mutable = data._mutable
        data._mutable = True

        if 'draft' not in data or data['draft'] is False:
            data['saved'] = datetime.now()

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

        filter_type = data['filter_type'] if 'filter_type' in data else 'all'

        sort = data['sort'] if 'sort' in data else 'desc'
        sort_type = 'created' if sort == 'asc' else '-created'

        user = request.user

        queryset = self.filter_queryset(self.get_queryset())

        if filter_type == 'all':
            queryset = queryset.filter(user=user)

        if filter_type == 'myphotos':
            queryset = queryset.filter(user=user, saved__isnull=False)

        if filter_type == 'mydrafts':
            queryset = queryset.filter(user=user, saved=None)

        queryset = queryset.order_by(sort_type)
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        print(request.data)
        user = request.data

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)