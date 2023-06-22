
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from teachers.models import Teacher

#Serializers
from teachers.serializers import TeacherSerializer, TeacherModelSerializer


class TeacherViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = TeacherModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        data = TeacherModelSerializer(teacher).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset