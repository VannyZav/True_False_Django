from django.core.validators import RegexValidator
from rest_framework import serializers
from api.models import ApiUser, Product, User


phone_validator = RegexValidator(regex=r'^\d{7,20}$', message='Номер телефона должен содержать только цифры и быть длиной от 7 до 20 символов')


class UserSerializer(serializers.ModelSerializer):
    agrees_to_policy = serializers.BooleanField(write_only=True)
    phone = serializers.CharField(validators=[phone_validator])

    def validate_phone(self, value):
        # if User.objects.filter(phone=value).exists():
        #     raise serializers.ValidationError("Этот номер телефона уже зарегистрирован.")
        phone_validator(value)
        return value

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'agrees_to_policy', 'play']

    def validate_agrees_to_policy(self, value):
        if not value:
            raise serializers.ValidationError("Вы должны согласиться с политикой обработки данных.")
        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        user, created = User.objects.get_or_create(email=email, defaults=validated_data)
        if not created:
            user.name = validated_data.get('name')
            user.phone = validated_data.get('phone')
            user.play = True
            user.save()
        return user




    # def create(self, validated_data):
    #
    #     agrees_to_policy = validated_data.pop('agrees_to_policy')
    #     user = User.objects.create(**validated_data, agrees_to_policy=agrees_to_policy)
    #     return user


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "firstInfo", "secondInfo", "image"]
        extra_kwargs = {"id": {"read_only": True}}
