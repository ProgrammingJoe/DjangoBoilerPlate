from rest_framework import viewsets

from example.models import School
from example.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = ()
