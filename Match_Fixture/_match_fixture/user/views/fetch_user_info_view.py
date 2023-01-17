from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


class FetchUserInfoView(APIView):
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        # email and password
        user = request.user
        return Response({"id" : user.id, "email" : user.email}, status = 200)