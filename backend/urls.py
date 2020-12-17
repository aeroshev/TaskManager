from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    re_path(
        r'^(?!admin|api|docs|media|static).*',
        TemplateView.as_view(template_name='index.html')
    ),
    path(r'api/', include('api.urls')),
    path(r'docs/', include_docs_urls()),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
]
urlpatterns += staticfiles_urlpatterns()
