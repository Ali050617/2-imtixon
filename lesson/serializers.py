from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'model', 'title', 'content', 'video_url',
                  'duration', 'order', 'created_at', 'updated_at')

