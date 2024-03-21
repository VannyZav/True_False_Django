from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ApiUser, Product, User
from api.serializers import ApiUserSerializer, ProductSerializer, UserSerializer


class ApiUserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'patch', 'get']
    serializer_class = ApiUserSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['post', 'patch', 'get', 'delete']
    serializer_class = ProductSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['post', 'patch', 'get', 'delete']
    serializer_class = UserSerializer


