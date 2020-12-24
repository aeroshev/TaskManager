from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers

from core.models import TMAbstractUser, TMUser

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TMUser
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserSerializer(required=False)

    def create(self, validated_data: dict) -> TMAbstractUser:
        profile_data = validated_data.pop('tm_user')
        user = TMAbstractUser.objects.create_user(**validated_data)
        TMUser.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender']
        )
        return user

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = TMAbstractUser
        fields = ('email', 'password', 'tm_user')
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data: dict) -> dict:
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password is not found."
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except TMAbstractUser.DoesNotExist:
            raise serializers.ValidationError(
                "User with given email and password does not exists"
            )
        return {
            'email': user.email,
            'token': jwt_token
        }



