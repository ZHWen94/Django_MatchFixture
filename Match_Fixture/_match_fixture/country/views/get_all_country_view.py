from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from country.models.country import Country

class GetAllCountryView(APIView):
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        # get all country 
        country_qs = Country.objects.filter(is_deleted = False)
        return Response({"result": self.gen_resp(country_qs)}, status=200)

    def gen_resp(self, qs):
        resp = []
        for data in qs:
            resp.append({"id": data.id, "name": data.name, "flag": data.flag, "continent": data.continent})
        return resp