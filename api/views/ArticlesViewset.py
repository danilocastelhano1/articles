from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from api.models.ArticlesModel import Articles

from api.serializers.ArticlesSerializers import ArticlesSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from url_filter.filtersets import ModelFilterSet


class ArticlesFilter(ModelFilterSet):
    class Meta:
        model = Articles


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = '-id'
    filter_class = ArticlesFilter
    permission_classes = [IsAuthenticated]
