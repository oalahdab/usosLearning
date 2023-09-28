"""
Views for the course APIs.
"""
from rest_framework.authentication import  BasicAuthentication

from rest_framework import viewsets

from usosLearning.models import Course
from course import serializers


class CourseViewSet(viewsets.ModelViewSet):
    """View for manage course APIs."""
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [BasicAuthentication]