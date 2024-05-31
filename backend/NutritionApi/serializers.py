from rest_framework import serializers
from .models import RecipeNutrition


class RecipeNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeNutrition
        fields = '__all__'
