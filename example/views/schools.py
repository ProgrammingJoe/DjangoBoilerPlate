from rest_framework import viewsets

from example.models import School, District
from example.serializers import SchoolSerializer, DistrictSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = ()


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = ()
