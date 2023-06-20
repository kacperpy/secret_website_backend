from django.db import router
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from list.api.views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')


urlpatterns = [
    path('', include(router.urls)),
]
