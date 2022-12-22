from rest_framework import routers
from django.urls import path

from example.views import SchoolViewSet, DistrictViewSet
from example.views.config import get_constants

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'districts', DistrictViewSet)

urlpatterns = [
    path('constants/', get_constants, name='constant')
]
