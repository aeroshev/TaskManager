from django.urls import include, path

from rest_framework_nested import routers

from api.views.members import MemberViewSet
from api.views.tasks import TaskViewSet
from api.views.teams import TeamViewSet
from api.views.users import UserViewSet, UserRegistrationView, UserLoginView
from api.views.projects import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'members', MemberViewSet, basename='members')
router.register(r'projects', ProjectViewSet, basename='projects')

auth_router = routers.DefaultRouter()
auth_router.register(r'signup', UserLoginView, basename='signup')
auth_router.register(r'signin', UserRegistrationView, basename='signin')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(auth_router.urls))
]
