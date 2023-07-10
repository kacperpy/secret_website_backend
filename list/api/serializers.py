from rest_framework import serializers

from list.core.tools import get_formatted_date
from list.models import Movie


class MovieReadSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'uuid',
            'origin_room',
            'title',
            'description',
            'description_long',
            'image_url',
            'image_file',
            'created_at',
        ]

    def get_created_at(self, instance):
        return get_formatted_date(instance.created_at)


class MovieCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'description_long',
            'image_url'
        ]
