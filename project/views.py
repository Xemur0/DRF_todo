from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
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





