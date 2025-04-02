from rest_framework import viewsets, permissions
from .models import Lesson
from .serializers import LessonSerializer
from .paginations import LessonPagination


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = LessonPagination
    permission_classes = [permissions.AllowAny]

