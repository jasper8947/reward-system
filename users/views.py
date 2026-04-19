from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from drf_spectacular.utils import extend_schema

from .models import PointTransaction
from .serializers import RegisterSerializer, TopUpSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class TopUpView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=TopUpSerializer,
        responses={200: TopUpSerializer}, 
    )
    def post(self, request):
        serializer = TopUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data["amount"]

        with transaction.atomic():
            user = request.user
            user.points += amount
            user.save()

            PointTransaction.objects.create(
                user=user,
                amount=amount,
                type="topup"
            )

        return Response({
            "message": "Top up success",
            "points": user.points
        })