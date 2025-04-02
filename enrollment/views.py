from rest_framework import viewsets, permissions
from .models import Enrollment
from .serializers import EnrollmentSerializer
from .paginations import EnrollmentPagination


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = EnrollmentPagination
