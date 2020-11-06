from rest_framework.viewsets import ModelViewSet

from api.serializers.users import UserSerializer
from core.models.users import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
