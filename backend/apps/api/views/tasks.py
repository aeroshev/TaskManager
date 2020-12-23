from rest_framework.viewsets import ModelViewSet

from api.paginations.common import StandardResultsSetPagination
from api.serializers.tasks import TaskSerializer
from core.models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination
