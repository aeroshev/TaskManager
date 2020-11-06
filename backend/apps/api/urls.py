from django.urls import include, path

from rest_framework_nested import routers

from api.views.members import MemberViewSet
from api.views.tasks import TaskViewSet
from api.views.teams import TeamViewSet
from api.views.users import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'members', MemberViewSet, basename='members')

urlpatterns = [
    path('', include(router.urls))
]
