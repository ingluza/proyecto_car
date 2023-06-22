# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from qualifications import views

router = DefaultRouter()
router.register(r'qualifications', views.QualificationViewSet, basename='qualifications')

urlpatterns = [
    path('', include(router.urls))
]