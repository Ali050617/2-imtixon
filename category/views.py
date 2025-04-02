from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer
from .paginations import CategoryPagination
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CategoryPagination
