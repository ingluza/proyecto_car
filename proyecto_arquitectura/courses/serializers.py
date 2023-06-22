# Django REST Framework
from rest_framework import serializers
# Model
from courses.models import Course

class CourseModelSerializer(serializers.ModelSerializer):
    """Course Model Serializer"""

    class Meta:
        """Meta class."""

        model = Course
        fields = (
            'name',
            'teacher_id',
            'description',
            'rating'
        )


class CourseSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=240)
    teacher_id = serializers.StringRelatedField(many=True)
    description = serializers.CharField()
    rating = serializers.CharField()

    def create(self, data):

        course = Course.objects.create(**data)
        return course
