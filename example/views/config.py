from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from example.models import School


def format_constants_and_options(constants):
    options_and_constants = {}

    option_list = []

    for item in constants:
        options_and_constants[item[1]] = item[0]
        option_list.append({
            'value': item[0],
            'label': item[1]
        })

    options_and_constants['options'] = option_list

    return options_and_constants


@api_view(['GET'])
@permission_classes([])
def get_constants(request):
    return Response({
        'schoolCategories': format_constants_and_options(School.HIGHSCHOOL_CATEGORY)
    }, status=status.HTTP_200_OK)
