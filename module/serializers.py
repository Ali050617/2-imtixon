from rest_framework import serializers
from .models import Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'course', 'title', 'order', 'created_at', 'updated_at')
