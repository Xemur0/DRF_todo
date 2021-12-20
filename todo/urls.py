"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView

from project.views import TodoModelViewSet, ProjectModelViewSet
from users.views import UserCustomViewSet

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('todo', TodoModelViewSet)
router.register('project', ProjectModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Todo',
        default_version='2',
        contact=openapi.Contact(email='aleks@gmail.com'),
        description='Documentation for Todo',
        license=openapi.License(name='Test'),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-user/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    path('swagger/<str:format>/', schema_view.without_ui()),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

]
