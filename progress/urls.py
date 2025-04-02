from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter
router.register(r'progress/', views.ProgressViewSet, basename='list_create_progress')

urlpatterns = [
    path('', include(router.urls))
]
