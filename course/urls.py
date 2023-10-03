"""
URL mappings for the course app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from .views import CoursesBySubjectView

from course import views

router = DefaultRouter()
router.register('course', views.CourseViewSet)

instructor_router = DefaultRouter()
instructor_router.register('instructor', views.InstructorViewSet)

app_name = 'course'

urlpatterns = [
    path('', include(router.urls)),
    path('courses/by_subject/<int:subject_number>/', CoursesBySubjectView.as_view(), name='endpoint-1'),
    path('api/', include(instructor_router.urls)),

]
