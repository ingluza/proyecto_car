# Django REST Framework
from rest_framework import serializers
# Model
from teachers.models import Teacher

class TeacherModelSerializer(serializers.ModelSerializer):
    """Teacher Model Serializer"""

    class Meta:
        """Meta class."""

        model = Teacher
        fields = (
            'identification',
            'name',
            'last_name',
            'email',
            'cellphone',
            'birth_date',
            'address'
        )


class TeacherSerializer(serializers.Serializer):

    identification = serializers.IntegerField()
    name = serializers.CharField(max_length=140)
    last_name = serializers.CharField(max_length=140)
    email = serializers.EmailField()
    cellphone = serializers.CharField(max_length=15, default=None)
    birth_date = serializers.DateField()
    address = serializers.CharField(max_length=240)

    def create(self, data):

        teacher = Teacher.objects.create(**data)
        return teacher
