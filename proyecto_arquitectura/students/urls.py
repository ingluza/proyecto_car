# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from students import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls))
]