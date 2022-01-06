from django.urls import include, path

from . import views

urlpatterns = [
    path('', include(views.urlpatterns)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
