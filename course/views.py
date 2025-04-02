from rest_framework import viewsets, permissions
from .models import Course
from .serializrs import CourseSerializer
from .paginations import CoursePagination


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CoursePagination
