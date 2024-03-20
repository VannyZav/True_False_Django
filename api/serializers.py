from django.core.validators import RegexValidator
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework import validators
from rest_framework.exceptions import ValidationError
from api.models import ApiUser, Product


# class UserSerializer(serializers.Serializer):
#     # username = serializers.CharField(max_length=128)
#     email = serializers.EmailField(validators=[
#         validators.UniqueValidator(ApiUser.objects.all())
#     ])
#     password = serializers.CharField(min_length=6, max_length=20, write_only=True)
#     privacy_policy_agreement = serializers.BooleanField()
#
#     def validate_privacy_policy_agreement(self, value):
#         if not value:
#             raise ValidationError("You must agree to the privacy policy.")
#         return value
#
#     def update(self, instance, validated_data):
#         if email := validated_data.get("email"):
#             instance.email = email
#             instance.save(update_fields=["email"])
#
#         if password := validated_data.get("password"):
#             instance.set_password(password)
#             instance.save(update_fields=["password"])
#         return instance

    # def create(self, validated_data):
    #
    #     if validated_data["privacy_policy_agreement"] != True:
    #         raise ValidationError("You must agree to the privacy policy.")
    #
    #     user = ApiUser.objects.create(
    #         # privacy_policy_egreement=validated_data["privacy_policy_agreement"],
    #         # username=validated_data["username"],
    #         email=validated_data["email"]
    #     )
    #
    #     user.set_password(validated_data["password"])
    #     user.save(update_fields=["password"])
    #     return user

#
# phone_validator = RegexValidator(regex=r'^\d{7,20}$', message='Номер телефона должен содержать только цифры и быть длиной от 7 до 20 символов')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     agrees_to_policy = serializers.BooleanField(write_only=True)
#     phone = serializers.CharField(validators=[phone_validator])
#
#     def validate_phone(self, value):
#         if ApiUser.objects.filter(phone=value).exists():
#             raise serializers.ValidationError("Этот номер телефона уже зарегистрирован.")
#         phone_validator(value)
#         return value
#
#     class Meta:
#         model = ApiUser
#         fields = ['id', 'name', 'email', 'phone', 'agrees_to_policy']
#
#     def validate_agrees_to_policy(self, value):
#         if not value:
#             raise serializers.ValidationError("Вы должны согласиться с политикой обработки данных.")
#         return value
#
#     def create(self, validated_data):
#         agrees_to_policy = validated_data.pop('agrees_to_policy')
#         user = ApiUser.objects.create(**validated_data, agrees_to_policy=agrees_to_policy)
#         return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "exists"]
        extra_kwargs = {"id": {"read_only": True}}
