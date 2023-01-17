from rest_framework import serializers

class OtpVerifyRequest(serializers.Serializer):
    email = serializers.EmailField(max_length=300)
    otp_val = serializers.IntegerField()