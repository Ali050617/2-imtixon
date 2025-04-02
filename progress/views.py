from rest_framework import viewsets, permissions
from .models import Progress
from .serializers import ProgressSerializer
from .paginations import ProgressPagination


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ProgressPagination

