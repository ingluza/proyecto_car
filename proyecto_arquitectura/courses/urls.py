# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from courses import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls))
]