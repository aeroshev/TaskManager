from rest_framework.viewsets import ModelViewSet

from api.serializers.tasks import TaskSerializer
from core.models.tasks import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
