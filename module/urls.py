from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter
router.register(r'module/', views.ModuleViewSet, basename='list_create_module')

urlpatterns = [
    path('', include(router.urls))
]