from rest_framework import serializers

class LoginRequest(serializers.Serializer):
    email = serializers.EmailField(max_length=300)
    password = serializers.CharField(max_length=100)