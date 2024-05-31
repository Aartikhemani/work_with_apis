from django.db import models


class RecipeNutrition(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField(null=True, blank=True)
    nutrition_data = models.JSONField(null=True, blank=True)
#     calories = models.FloatField(null=True, blank=True)
#     protein = models.FloatField(null=True, blank=True)
#     fat = models.FloatField(null=True, blank=True)
#     carbohydrates = models.FloatField(null=True, blank=True)
