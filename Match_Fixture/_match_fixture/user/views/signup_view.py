from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models.user import User
from user.models.otp import Otp
from user.serializer.signup_req import SignupRequest
from user.serializer.user_serializer import UserSerializer

class SingupView(APIView):
    def post(self, request):
        # validate request data
        req = self.validated_data(request=request)
        # check if user already exists
        if User.objects.filter(email=req["email"]).exists():
            return Response({"Error": "User already exists!"}, status=400)
        # create and get new user instance
        user_instance = UserSerializer.create(validated_data=req)
        # create otp
        otp_val = self.gen_otp(user_instance=user_instance)
        return Response({"id": user_instance.id, "email": user_instance.email, "otp_val": otp_val}, status=200)

    # data validate method
    def validated_data(self, request):
        req = SignupRequest(data = request.data)
        req.is_valid(raise_exception=True)
        return req.validated_data

    # otp generation method
    def gen_otp(self, user_instance):
        import random
        otp_val = random.randint(10000, 99999)
        Otp.objects.create(user=user_instance, otp_val=otp_val)
        return otp_val
        