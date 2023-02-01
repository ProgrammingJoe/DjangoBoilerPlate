from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from example.models import School


def convert_constants_to_dropdown_format(constants):
    option_list = []

    for item in constants:
        option_list.append({
            'value': item[0],
            'label': item[1]
        })

    return option_list


@api_view(['GET'])
@permission_classes([])
def get_constants(request):
    return Response({
        'schoolCategories': convert_constants_to_dropdown_format(School.HIGHSCHOOL_CATEGORY)
    }, status=status.HTTP_200_OK)
