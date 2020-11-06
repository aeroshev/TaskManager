from rest_framework.viewsets import ModelViewSet

from api.serializers.members import MemberSerializer
from core.models.members import Member


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
