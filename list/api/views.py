from rest_framework import mixins, viewsets
from list.api.serializers import MovieReadSerializer
from rest_framework.permissions import IsAuthenticated

from list.models import Movie


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieReadSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'
