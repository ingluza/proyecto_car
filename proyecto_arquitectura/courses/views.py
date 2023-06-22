
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from courses.models import Course

#Serializers
from courses.serializers import CourseModelSerializer, CourseSerializer


class CourseViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = CourseModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        course = serializer.save()
        data = CourseModelSerializer(course).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        queryset = Course.objects.all()
        return queryset