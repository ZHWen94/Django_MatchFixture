from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from country.models.country import Country
from country.serializer.create_country_req import CreateCountryRequest

class CreateCountryView(APIView):
    permission_classes = [(IsAuthenticated)]

    def post(self, request):
        # validate request data
        req = self.validated_data(request=request)
        # check if country already exists
        check_country = Country.objects.filter(name=req["name"])
        if check_country.exists():
            # return error and existsed country id
            return Response({"Error": "Country already exists! Please update or delete the country!", "Country_id": check_country[0].id}, status=400)
        user = request.user
        # create country
        instance = Country.objects.create(name=req["name"], flag=req["flag"], continent=req["continent"], created_by=user, created_at=datetime.now())
        return Response({"id": instance.id, "name": instance.name, "flag": instance.flag, "continent": instance.continent, "editor": instance.created_by.id}, status=200)

    # data validate method
    def validated_data(self, request):
        req = CreateCountryRequest(data = request.data)
        req.is_valid(raise_exception=True)
        return req.validated_data