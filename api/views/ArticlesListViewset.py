from rest_framework import viewsets, mixins

from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from api.models.ArticlesModel import Articles

from api.serializers.ArticlesSerializers import ArticlesSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from url_filter.filtersets import ModelFilterSet


class ArticlesListFilter(ModelFilterSet):
    class Meta:
        model = Articles


class ArticleListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = '-id'
    filter_class = ArticlesListFilter
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        exclude = ["summary"]
        if not request.user.is_authenticated:
            self.serializer_class.Meta.fields = [f.name for f in self.serializer_class.Meta.model._meta.fields if
                                                f.name not in exclude]
        else:
            self.serializer_class.Meta.fields = [f.name for f in self.serializer_class.Meta.model._meta.fields]

        queryset = Articles.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
