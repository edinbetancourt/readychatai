""" project URL Configuration """

# Sistem import
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('', include('api.urls')),
    path('', include('todo.urls')),

    # Spectacular patterns
    path('doc/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('doc/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
