# Django REST Framework
from rest_framework import serializers
# Model
from students.models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    """Student Model Serializer"""

    class Meta:
        """Meta class."""

        model = Student
        fields = (
            'identification',
            'name',
            'last_name',
            'email',
            'cellphone',
            'birth_date',
            'address'
        )


class StudentSerializer(serializers.Serializer):

    identification = serializers.IntegerField()
    name = serializers.CharField(max_length=140)
    last_name = serializers.CharField(max_length=140)
    email = serializers.EmailField()
    cellphone = serializers.CharField(max_length=15, default=None)
    birth_date = serializers.DateField()
    address = serializers.CharField(max_length=240)

    def create(self, data):

        student = Student.objects.create(**data)
        return student
