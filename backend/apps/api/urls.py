from django.urls import include, path

from rest_framework_nested import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]
