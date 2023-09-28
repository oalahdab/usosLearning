"""Serializers for course APIs
"""
from rest_framework import serializers

from usosLearning.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for courses."""

    class Meta:
        model = Course
        fields = ['id', 'instructor','title','description','lessonCount',
                  'subject','imageURL','lastUpdate','duration','enrollmentCount',
                  'targetAudience','videoURL','language','price','discount']
        read_only_fields = ['id']
