from rest_framework import viewsets

from api.models import ApiUser
from api.serializers import UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'patch', 'get']
    serializer_class = UserSerializer

