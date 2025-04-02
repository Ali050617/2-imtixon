from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'teacher', 'category', 'price',
                  'discount_price', 'image', 'is_published', 'created_at', 'updated_at')
        filter = ('title', 'category', 'price')