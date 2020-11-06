from django.urls import include, path

from rest_framework_nested import routers

from api.views.users import UserViewSet
from api.views.teams import TeamViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('', include(router.urls))
]
