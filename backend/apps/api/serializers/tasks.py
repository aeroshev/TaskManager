from rest_framework.serializers import ModelSerializer

from core.models.tasks import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
