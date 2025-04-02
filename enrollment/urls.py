from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter
router.register(r'enrollments/', views.EnrollmentViewSet, basename='list_create_enrollment'),

urlpatterns = [
    path('', include(router.urls)),
]