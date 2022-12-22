from rest_framework import serializers

from example.models import School, District


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'category', 'district']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'code']
