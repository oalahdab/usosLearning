"""Serializers for course APIs
"""
from rest_framework import serializers

from usosLearning.models import Course, Instructor, Tag

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for courses."""

    tags = TagSerializer(many=True, required=False)
    class Meta:
        model = Course
        fields = ['id', 'instructor','title','description','lessonCount',
                  'subjectId','imageURL','lastUpdate','duration','enrollmentCount',
                  'targetAudience','videoURL','language','price','discount', 'tags']
        read_only_fields = ['id']
        
    def _get_or_create_tags(self, tags, course):
        """Handle getting or creating tags as needed."""
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                **tag,
            )
            course.tags.add(tag_obj)

    def create(self, validated_data):
        """Create a course."""

        tags = validated_data.pop('tags', [])
        course = Course.objects.create(**validated_data)
        self._get_or_create_tags(tags, course)

        return course

    def update(self, instance, validated_data):
        """Update course"""
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class InstructorSerializer(serializers.ModelSerializer):
    """Serializers for instructors"""

    class Meta:
        model = Instructor
        fields = ['id', 'fullName', 'profession', 'imageURL', 
                  'socialMediaLink1', 'socialMediaLink2']
        read_only_fields = ['id']

