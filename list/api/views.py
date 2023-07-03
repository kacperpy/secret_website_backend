from io import BytesIO
from rest_framework import mixins, viewsets
from list.api.serializers import MovieReadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests
from django.core.files.uploadedfile import UploadedFile
from list.models import Movie
from datetime import datetime


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def perform_create(self, serializer):
        image_url = serializer.validated_data.get('image_url')
        image_file_name = f"{serializer.validated_data.get('title')}_{datetime.now()}.jpg"

        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            return Response({'error': 'Failed to download image'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(image_file=UploadedFile(
            BytesIO(image_response.content), name=image_file_name))
