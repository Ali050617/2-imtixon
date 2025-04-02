from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses_list_create'),

urlpatterns = [
    path('', include(router.urls)),
]