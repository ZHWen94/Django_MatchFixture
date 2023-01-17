from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from user.models.user import User
from user.models.otp import Otp
from user.serializer.login_req import LoginRequest

class LoginView(APIView):
    def post(self, request):
        # validate request data
        req = self.validated_data(request)
        email = req["email"]
        password = req["password"]
        # get user
        user_qury = User.objects.filter(email=email)
        # check user exists
        if user_qury.exists():
            user = user_qury[0]
            # check otp status
            if user.otp_status:
                # check password
                if user.check_password(password):
                    token, create = Token.objects.get_or_create(user=user)
                    return Response({"key": token.key}, status=200)
                # return error if password not match
                else:
                    return Response({"Error": "Invalid password!"}, status=400)
            # return error if otp not verified
            else:
                return Response({"Error": "Otp not verified!"}, status=400)
        # return error if user not exists
        else:
            return Response({"Error": "User not exists!"}, status=400)

    # data validate method
    def validated_data(self, request):
        req = LoginRequest(data = request.data)
        req.is_valid(raise_exception=True)
        return req.validated_data