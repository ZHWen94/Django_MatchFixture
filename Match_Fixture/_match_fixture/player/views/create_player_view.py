from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from player.models.player import Player
from country.models.country import Country
from player.serializer.create_player_req import CreatePlayerRequest

class CreatePlayerView(APIView):
    permission_classes = [(IsAuthenticated)]

    def post(self, request):
        # validate request data
        req = self.validated_data(request=request)
        # check if player already exists
        check_player = Player.objects.filter(name=req["name"])
        if check_player.exists():
            # return error and existsed country id
            return Response({"Error": "Player already exists! Please update or delete the country!", "Player_id": check_player[0].id}, status=400)
        # get country data
        country_query = Country.objects.filter(name=req["country_name"], is_deleted=False)
        if country_query.exists():
            # get country object
            country = country_query[0]
            # get dob datetime object
            dob_str = req["dob"]
            dob_obj = datetime.strptime(dob_str, '%m-%d-%Y').date()
            # create player
            user = request.user
            instance = Player.objects.create(name=req["name"], country_id=country.id, image=req["image"], dob=dob_obj, status=req["status"], height=req["height"], weight=req["weight"], created_by=user, created_at=datetime.now())
            return Response({"id": instance.id, "name": instance.name, "country":instance.country.name, "image": instance.image, "dob": instance.dob, "status": instance.status, "height": instance.height, "weight": instance.weight, "editor": user.id}, status=200)
        else:
            return Response({"Error": "Country not exists in db"}, status=400)

    # data validate method
    def validated_data(self, request):
        req = CreatePlayerRequest(data = request.data)
        req.is_valid(raise_exception=True)
        return req.validated_data