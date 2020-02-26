from django.conf.urls import url
from django.urls import include
from photos.views import PhotosView
from photos.views import PhotosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', PhotosViewSet)

urlpatterns = [
    url(r'^photos/$', PhotosView.as_view(), kwargs={'pk': None}),
    url(r'^photos/(?P<photo_id>[0-9]+)', PhotosView.as_view()),
    url(r'^photos/list', include(router.urls))
]