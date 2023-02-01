from django_filters import rest_framework as filters
from example.models import School
from django.db.models import Count


def quantity_gte_filter(qs, name, value):
    return qs.annotate(
        number_of_item=Count(name)
    ).filter(number_of_item__gte=value)


def quantity_lte_filter(qs, name, value):
    return qs.annotate(
        number_of_item=Count(name)
    ).filter(number_of_item__lte=value)


def quantity_exact_filter(qs, name, value):
    return qs.annotate(
        number_of_item=Count(name)
    ).filter(number_of_item=value)


class SchoolFilter(filters.FilterSet):
    students__gte = filters.NumberFilter(method=quantity_gte_filter, field_name='students')
    students__lte = filters.NumberFilter(method=quantity_lte_filter, field_name='students')
    students__exact = filters.NumberFilter(method=quantity_exact_filter, field_name='students')

    class Meta:
        model = School
        fields = ['category']
