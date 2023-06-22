# Django REST Framework
from rest_framework import serializers
# Model
from qualifications.models import Qualification

class QualificationModelSerializer(serializers.ModelSerializer):
    """Qualification Model Serializer"""

    class Meta:
        """Meta class."""

        model = Qualification
        fields = (
            'student_id',
            'course_id',
            'score'
        )


class QualificationSerializer(serializers.Serializer):

    student_id = serializers.StringRelatedField(many=True)
    course_id = serializers.StringRelatedField(many=True)
    score = serializers.DecimalField(max_digits=3, decimal_places=2)

    def create(self, data):

        qualification = Qualification.objects.create(**data)
        return qualification
