from rest_framework import routers

from example.views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)

urlpatterns = []
