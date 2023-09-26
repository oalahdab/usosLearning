"""
Tests for courses api.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from usosLearning.models import Course

from course.serializers import CourseSerializer


# COURSE_URL == reverse('course:course-list')


def create_course(user, **params):
    """Create and return a sample course.""" 
    defaults = {
        "instructor": "Nurullah Nahhas",
        "title": "Angular Full Complete Course",
        "description": "Fake Description was a writing mini-contest in which you had to write your own funny and genuine description for one of the turrets from the Garage. Your description then had to be submitted via a special form. The entries were judged by their level of creativity and humor.",
        "lessonCount": "350",
        "subject": "Devlopmet",
        "imageURL": "https://repository-images.githubusercontent.com/24195339/87018c00-694b-11e9-8b5f-c34826306d36",
        "lastUpdate": "2023-09-18T11:13:54.393",
        "duration": "20",
        "enrollmentCount": 400,
        "targetAudience": "Finish the course",
        "videoURL": "https://www.youtube.com/watch?v=_qAJMXfL6o0",
        "language": "English",
        "price": 30,
        "discount": 0
    }
    defaults.update(params)

    course = Course.objects.create(**defaults)
    return course


class PublicCourseAPITests(TestCase):
    """Test Course API requests"""
    def test_retrieve_course(self):
        create_course()
        create_course()

        