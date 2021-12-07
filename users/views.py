from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserModelSerializer

# class UserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer

class UserCustomViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]