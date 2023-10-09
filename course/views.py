"""
Views for the course APIs.
"""
from rest_framework.authentication import  BasicAuthentication
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from usosLearning.models import Course,Instructor, Tag

from course import serializers
from course.pagination import CustomPageNumberPagination

from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """View for manage course APIs."""
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [BasicAuthentication]
    pagination_class = CustomPageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response_data = {
                'total_pages': self.paginator.page.paginator.num_pages,  # Add total page count
                'results': serializer.data,
            }
            return self.get_paginated_response(response_data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CoursesBySubjectView(ListAPIView):
    """Get couses by subject"""
    serializer_class = CourseSerializer
    pagination_class = None

    def get_queryset(self):
        subjectId = self.kwargs['subjectId']
        queryset = Course.objects.filter(subjectId=subjectId)
        return queryset

class InstructorViewSet(viewsets.ModelViewSet):
    """View for manage course APIs."""
    serializer_class = serializers.InstructorSerializer
    queryset = Instructor.objects.all()
    authentication_classes = [BasicAuthentication]
    pagination_class = None

class TagViewSet(mixins.UpdateModelMixin, 
                 mixins.ListModelMixin, 
                 viewsets.GenericViewSet,
                 mixins.DestroyModelMixin):
    """Manage tags in the database"""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [BasicAuthentication]
    pagination_class = None
