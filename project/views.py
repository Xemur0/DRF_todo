from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, ToDoFilter
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class LimitListForProject(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = LimitListForProject
    filterset_class = ProjectFilter


class LimitListForTodo(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = LimitListForTodo
    filterset_class = ToDoFilter

    def destroy(self, request, *args, **kwargs):

        todo = self.get_object()
        if todo.is_active == True:
            todo.is_active = False
            todo.save()
        elif todo.is_active == False:
            todo.is_active = True
            todo.save()
        return Response(status=status.HTTP_200_OK)
