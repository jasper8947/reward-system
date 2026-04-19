from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .serializers import RedeemSerializer
from .services import redeem_product


class RedeemView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=RedeemSerializer)
    def post(self, request):
        serializer = RedeemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data["product_id"]

        redeem_product(request.user, product_id)

        return Response({"message": "OK"})