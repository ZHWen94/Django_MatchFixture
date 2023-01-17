from rest_framework import serializers

class UpdateCountryRequest(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    flag = serializers.CharField(max_length=300)
    continent = serializers.CharField(max_length=100)