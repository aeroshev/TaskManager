from rest_framework.viewsets import ModelViewSet

from api.serializers.teams import TeamSerializer
from core.models import Team


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
