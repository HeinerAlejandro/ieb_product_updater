from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .models import Product
from .serializers import ProductSerializer


# Create your views here.


class ProductReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = [
        'buying_price',
        'selling_price',
        'description'
    ]
    ordering_fields = [
        'buying_price',
        'selling_price',
        'description'
    ]
