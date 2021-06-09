from rest_framework import serializers

from api.models.ArticlesModel import Articles
from api.models.AuthorsModel import Authors
from api.serializers.AuthorsSerializers import AuthorsSerializer


class ArticlesSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Authors.objects)

    class Meta:
        model = Articles
        fields = (
            'id', 'author', 'category', 'title', 'summary'
        )

    def to_representation(self, instance):
        data = super(ArticlesSerializer, self).to_representation(instance)
        author_serializer = AuthorsSerializer(instance.author)

        data['author'] = author_serializer.data

        return data
