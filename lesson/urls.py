from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter
router.register(r'lessons/', views.LessonViewSet, basename='list_create_lessons'),

urlpatterns = [
    path('', include(router.urls)),
]