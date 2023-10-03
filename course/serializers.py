"""Serializers for course APIs
"""
from rest_framework import serializers

from usosLearning.models import Course, Instructor

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for courses."""

    class Meta:
        model = Course
        fields = ['id', 'instructor','title','description','lessonCount',
                  'subjectId','imageURL','lastUpdate','duration','enrollmentCount',
                  'targetAudience','videoURL','language','price','discount']
        read_only_fields = ['id']


class InstructorSerializer(serializers.ModelSerializer):
    """Serializers for instructors"""

    class Meta:
        model = Instructor
        fields = ['id', 'fullName', 'profession', 'imageURL', 
                  'socialMediaLink1', 'socialMediaLink2']
        read_only_fields = ['id']
