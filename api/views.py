from random import random

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ApiUser, Product
from api.serializers import UserSerializer, ProductSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'patch', 'get']
    serializer_class = UserSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['post', 'patch', 'get', 'delete']
    serializer_class = ProductSerializer

