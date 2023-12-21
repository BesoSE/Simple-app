from django.urls import re_path as url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from simple_app.views.average_greet import AverageView, GreetView


schema_view = get_schema_view(
    openapi.Info(
        title="Simple API",
        default_version='v1',
        description="Simple API",
        contact=openapi.Contact(email="semso2612@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^average/?$', AverageView.as_view(), name='average'),
    url(r'^greet/?$', GreetView.as_view(), name='greet'),
    url(r'^redoc/?$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^swagger/?$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
