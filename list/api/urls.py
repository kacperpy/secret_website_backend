from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from list.api.views import (AddToWatchlistAPIView, MovieCommentsListAPIView, MovieCreateCommentAPIView, MovieViewSet,
                            RemoveFromWatchListAPIView,
                            UserActiveMoviesListAPIView, UserMoviesListAPIView)

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')


urlpatterns = [
    path('', include(router.urls)),

    path(
        "user-movies/",
        UserMoviesListAPIView.as_view(),
        name="user-movie-list-all"
    ),
    path(
        "user-active-movies/",
        UserActiveMoviesListAPIView.as_view(),
        name="user-movie-list-active"
    ),
    path(
        "movies/<uuid:uuid>/remove-from-watchlist/",
        RemoveFromWatchListAPIView.as_view(),
        name="movie-remove-from-watchlist"
    ),
    path(
        "movies/<uuid:uuid>/add-to-watchlist/",
        AddToWatchlistAPIView.as_view(),
        name="movie-add-to-watchlist"
    ),
    path(
        "movies/<uuid:uuid>/comments/",
        MovieCommentsListAPIView.as_view(),
        name="movie-comment-list"
    ),
    path(
        "movies/<uuid:uuid>/create-comment/",
        MovieCreateCommentAPIView.as_view(),
        name="movie-create-comment"
    )
]
