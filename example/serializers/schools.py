from rest_framework import serializers

from example.models import School, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'code']


class SchoolSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    district_id = serializers.IntegerField()

    class Meta:
        model = School
        fields = ['name', 'category', 'district', 'district_id']
