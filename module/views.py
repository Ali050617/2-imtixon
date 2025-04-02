from rest_framework import viewsets, permissions
from .models import Module
from .serializers import ModuleSerializer
from .paginations import ModulePagination


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ModulePagination

