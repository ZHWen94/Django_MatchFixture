import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from country.models.country import Country
from country.serializer.update_country_req import UpdateCountryRequest

class UpdateCountryView(APIView):
    permission_classes = [(IsAuthenticated)]

    def put(self, request):
        # validate request data
        req = self.validated_data(request=request)
        # check if country already exists
        check_country = Country.objects.filter(name=req["name"])
        if check_country.exists():
            # return error and existsed country id
            return Response({"Error": "Country already exists! Please update or delete the country!", "Country_id": check_country[0].id}, status=400)
        # update and return response 
        Country.objects.filter(id=req["id"]).update(name=req["name"], flag=req["flag"], continent=req["continent"], updated_at=datetime.datetime.now())
        return Response({"Msg": "Country updated!"}, status=200)

    # data validate method
    def validated_data(self, request):
        req = UpdateCountryRequest(data = request.data)
        req.is_valid(raise_exception=True)
        return req.validated_data