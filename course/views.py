"""
Views for the course APIs.
"""
from rest_framework import viewsets

from usosLearning.models import Course
from course import serializers


class CourseViewSet(viewsets.ModelViewSet):
    """View for manage course APIs."""
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
