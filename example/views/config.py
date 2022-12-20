from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from example.models import School


@api_view(['GET'])
@permission_classes([])
def get_constants(request):
    return Response({
        'highschoolCategories': dict(School.HIGHSCHOOL_CATEGORY)
    }, status=status.HTTP_200_OK)
