from datetime import datetime
from io import BytesIO

import requests
from django.core.files.uploadedfile import UploadedFile
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from list.api.serializers import CommentCreateSerializer, CommentReadSerializer, MovieCreateSerializer, MovieReadSerializer
from list.models import Comment, Movie


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def perform_create(self, serializer):
        user_request = self.request.user
        room = user_request.room
        image_url = serializer.validated_data.get('image_url')
        image_file_name = f"{serializer.validated_data.get('title')}_{datetime.now()}.jpg"

        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            return Response({'error': 'Failed to download image'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(
            image_file=UploadedFile(
                BytesIO(image_response.content), name=image_file_name),
            origin_room=room
        )


class UserMoviesListAPIView(generics.ListAPIView):
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        request_room = request_user.room
        return request_room.movies.all()


class UserActiveMoviesListAPIView(generics.ListAPIView):
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        request_room = request_user.room
        return request_room.movies.filter(is_active=True)


class RemoveFromWatchListAPIView(APIView):
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, uuid):
        movie_request = get_object_or_404(Movie, uuid=uuid)
        movie_request.is_active = False
        movie_request.save()

        return Response(
            "Movie has been successfully removed from watchlist.",
            status=status.HTTP_200_OK
        )


class AddToWatchlistAPIView(APIView):
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, uuid):
        movie_request = get_object_or_404(Movie, uuid=uuid)
        movie_request.is_active = True
        movie_request.save()

        return Response(
            "Movie has been successfully added to watchlist.",
            status=status.HTTP_200_OK
        )


class MovieCommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_movie = get_object_or_404(Movie, uuid=self.kwargs.get('uuid'))
        return request_movie.comments.all()


class MovieCreateCommentAPIView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        movie_request = get_object_or_404(Movie, uuid=self.kwargs.get('uuid'))
        request_user = self.request.user
        serializer.save(
            movie=movie_request,
            created_by=request_user
        )
