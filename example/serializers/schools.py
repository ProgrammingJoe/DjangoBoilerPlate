from rest_framework import serializers
from rest_framework.serializers import ValidationError

from example.models import School, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'code']


class SchoolSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    district_id = serializers.IntegerField(write_only=True, required=True)
    number_of_students = serializers.SerializerMethodField()

    def get_number_of_students(self, obj):
        return obj.students.count()

    def validate(self, data):
        district_id = data['district_id']
        number_schools_in_district = School.objects.filter(district__id=district_id).count()

        if number_schools_in_district >= 10:
            raise ValidationError('Districts can have a maximum of 10 schools.')

        return data

    class Meta:
        model = School
        fields = [
            'name', 'category', 'district', 'district_id',
            'number_of_students'
        ]
