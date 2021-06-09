from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from api.models.AuthorsModel import Authors

from api.serializers.AuthorsSerializers import AuthorsSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from url_filter.filtersets import ModelFilterSet


class AuthorFilter(ModelFilterSet):
    class Meta:
        model = Authors


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = '-id'
    filter_class = AuthorFilter
