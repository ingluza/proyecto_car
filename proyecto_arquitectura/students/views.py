
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from students.models import Student

#Serializers
from students.serializers import StudentSerializer, StudentModelSerializer


class StudentViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = StudentModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        data = StudentModelSerializer(student).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset