from django.core.validators import RegexValidator
from rest_framework import serializers
from api.models import Product, User, ApiUser


"""Валидатор телефона"""
phone_validator = RegexValidator(
    regex=r'^\d{7,20}$',
    message='Номер телефона должен содержать \
    только цифры, быть длиной от 7 до 20 символов, введен без пробелов'
)


""" Сериализатор для создания пользователя, который участвует в игре. """
class UserSerializer(serializers.ModelSerializer):
    agrees_to_policy = serializers.BooleanField(write_only=True)
    phone = serializers.CharField(validators=[phone_validator])

    """ Функция валидация телефона """
    def validate_phone(self, value):
        phone_validator(value)
        return value

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'agrees_to_policy', "play"]
        extra_kwargs = {"play": {"read_only": True}}

    """Функция проверки на согласие обработки данных."""
    def validate_agrees_to_policy(self, value):
        if not value:
            raise serializers.ValidationError("Вы должны согласиться с политикой обработки данных.")
        return value

    """Метод создания пользователя: если пользователь вводит существующую почту, то остальные данные 
    перезаписываются, а поле play переводится с False на True, что значит, что пользователь уже играл в игру"""
    def create(self, validated_data):
        email = validated_data.get('email')
        user, created = User.objects.get_or_create(email=email, defaults=validated_data)
        if not created:
            user.name = validated_data.get('name')
            user.phone = validated_data.get('phone')
            user.play = True
            user.save()
        return user


"""Сериализатор для суперпользователя, возможно не нужный."""
class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


"""Сериализатор Продуктов"""
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "firstInfo", "secondInfo", "image"]
        extra_kwargs = {"id": {"read_only": True}}


"""Сериализатор для проверки ответа пользователя"""
class CheckProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=128)
    exists = serializers.BooleanField()
