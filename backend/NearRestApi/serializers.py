# serializers.py

from rest_framework import serializers


class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField()
    place_id = serializers.CharField()
    vicinity = serializers.CharField()
    rating = serializers.FloatField()
    types = serializers.ListField(child=serializers.CharField())
