from rest_framework import routers
from django.urls import path

from example.views import SchoolViewSet
from example.views.config import get_constants

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    path('constants', get_constants, name='constant')
]
