
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from qualifications.models import Qualification

#Serializers
from qualifications.serializers import QualificationSerializer, QualificationModelSerializer


class QualificationViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = QualificationSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = QualificationSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        qualification = serializer.save()
        data = QualificationModelSerializer(qualification).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        queryset = Qualification.objects.filter(id=id)
        return queryset