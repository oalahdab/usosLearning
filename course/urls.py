"""
URL mappings for the course app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from course import views

router = DefaultRouter()
router.register('course', views.CourseViewSet)
router.register('tags', views.TagViewSet)

instructor_router = DefaultRouter()
instructor_router.register('instructor', views.InstructorViewSet)

app_name = 'course'

urlpatterns = [
    path('', include(router.urls)),
    path('courses/by_subject/<int:subjectId>/',views.CoursesBySubjectView.as_view(), name='endpoint-1'),
    path('api/', include(instructor_router.urls)),
]
