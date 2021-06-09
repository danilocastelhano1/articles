from rest_framework import serializers
from api.models.AuthorsModel import Authors


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = (
            'id', 'name', 'picture'
        )
