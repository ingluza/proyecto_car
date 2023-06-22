# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from teachers import views

router = DefaultRouter()
router.register(r'teachers', views.TeacherViewSet, basename='teachers')

urlpatterns = [
    path('', include(router.urls))
]