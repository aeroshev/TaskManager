from rest_framework.viewsets import ModelViewSet

from api.serializers.projects import ProjectSerializer
from core.models import Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
