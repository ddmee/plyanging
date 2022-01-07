from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', include(views.urlpatterns)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
