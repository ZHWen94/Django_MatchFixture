from rest_framework import serializers

from country.models.country import Country

class CreatePlayerRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    country_name = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=300)
    dob = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    height = serializers.FloatField()
    weight = serializers.FloatField()