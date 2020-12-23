from rest_framework.viewsets import ModelViewSet

from api.serializers.users import UserSerializer
from core.models import TMUser


class UserViewSet(ModelViewSet):
    queryset = TMUser.objects.all()
    serializer_class = UserSerializer
