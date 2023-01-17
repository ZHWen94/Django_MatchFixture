from rest_framework import serializers

class SignupRequest(serializers.Serializer):
    email = serializers.EmailField(max_length=300)
    name = serializers.CharField(max_length=300)
    phone_num = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=100)
    