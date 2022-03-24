from rest_framework import serializers
from django.utils.six import text_type
from MilkShop.apps.authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', )


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for creating user objects"""
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = text_type(tokens)
        access = text_type(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user
