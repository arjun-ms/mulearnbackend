from decouple import config
from rest_framework.views import APIView

from db.organization import Organization, District
from utils.response import CustomResponse
from .serializer import OrganisationSerializer


class GetInstitutionsAPI(APIView):

    def get(self, request, organisation_type, district_name):
        protection_key = request.headers.get("protectionKey")
        if not protection_key or not protection_key == config('PROTECTED_API_KEY'):
            return CustomResponse(general_message="Invalid Key").get_failure_response()

        district = District.objects.filter(name=district_name).first()

        organisations = Organization.objects.filter(org_type=organisation_type, district=district)
        organisation_serializer = OrganisationSerializer(organisations, many=True)
        return CustomResponse(response={'institutions': organisation_serializer.data}).get_success_response()
