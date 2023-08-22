from rest_framework import viewsets

from djshop.apps.catalog.models import Category
from djshop.apps.catalog.serializers.front import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer