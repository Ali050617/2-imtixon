from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer
from .paginations import ReviewPagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    permission_classes = [permissions.AllowAny]

