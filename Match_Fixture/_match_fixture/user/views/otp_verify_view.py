from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models.user import User
from user.models.otp import Otp
from user.serializer.otp_verify_req import OtpVerifyRequest

class OtpVerifyView(APIView):
    def post(self, request):
        # validate request data
        req = self.validated_data(request)
        email = req["email"]
        otp_val = req["otp_val"]
        # get user
        user_query = User.objects.filter(email=email)
        # check user exists
        if user_query.exists():
            # get otp
            user = user_query[0]
            otp = Otp.objects.filter(user=user, otp_val=otp_val)
            # check otp
            if otp.exists():
                user_query.update(otp_status=True)
                return Response({"Msg": "Otp Verified!"}, status=200)
            # return error if otp not match
            else:
                return Response({"Error": "Invalid Otp!"}, status=400)
        # return error if user not exists
        else:
            return Response({"Error": "User not exists!"}, status=400)

    # data validate method
    def validated_data(self, request):
        req = OtpVerifyRequest(data = request.data)
        req.is_valid(raise_exception=True)
        return req.validated_data