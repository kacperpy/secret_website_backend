from django.db import router
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from list.api.views import MovieViewSet
from list.api.views import UserMoviesListAPIView

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')


urlpatterns = [
    path('', include(router.urls)),

    path(
        "user-movies/",
        UserMoviesListAPIView.as_view(),
        name="user-movie-list"
    )
]
