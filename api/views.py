from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product, User, ApiUser
from api.serializers import ProductSerializer, UserSerializer, CheckProductSerializer, ApiUserSerializer


"""Представление суперпользователя, не выдает и не забирает информацию, возможно лишняя"""
class ApiUserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = []
    serializer_class = ApiUserSerializer


"""Представление для получения продукта"""
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get']
    serializer_class = ProductSerializer


"""Представление для регистрации пользователя"""
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['post', 'patch']
    serializer_class = UserSerializer


"""Представление для проверки ответа пользователя. С фронта приходит название продукта и ответ пользователя,
который сверяется с полем exists у модели продукта"""
class CheckProductView(APIView):
    def post(self, request):
        serializer = CheckProductSerializer(data=request.data)
        if serializer.is_valid():
            product_name = serializer.validated_data['product_name']
            exists = serializer.validated_data['exists']

            try:
                product = Product.objects.get(name=product_name)
                if product.exists == exists:
                    response_data = {'message': 'Правильно', 'exists': product.exists}
                else:
                    response_data = {'message': 'Неправильно', 'exists': product.exists}
            except Product.DoesNotExist:
                response_data = {'message': 'Продукт не найден'}

            return Response(response_data)
        else:
            return Response(serializer.errors, status=400)
