from rest_framework import serializers

class RedeemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()