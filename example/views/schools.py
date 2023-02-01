from rest_framework import viewsets

from example.models import School, District
from example.serializers import SchoolSerializer, DistrictSerializer
from example.filters import SchoolFilter


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = ()
    filterset_class = SchoolFilter


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = ()
