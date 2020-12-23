from rest_framework.serializers import ModelSerializer

from core.models import TMUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = TMUser
        fields = '__all__'
