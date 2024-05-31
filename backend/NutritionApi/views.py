# views.py
import requests
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .forms import RecipeNutritionForm
from .models import RecipeNutrition
from .serializers import RecipeNutritionSerializer
from django.conf import settings
from .nutrition_api import get_nutrition_facts


def home(request):
    return render(request, 'NutritionApi/home.html')


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = RecipeNutrition.objects.all()
    serializer_class = RecipeNutritionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            nutrition_data = get_nutrition_facts(instance.ingredients)
            if nutrition_data:
                instance.nutrition_data = nutrition_data
                instance.save()
            else:
                print("No nutrition data returned")
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error retrieving nutrition data: {e}")


def recipe_form(request):
    if request.method == 'POST':
        form = RecipeNutritionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            nutrition_data = get_nutrition_facts(instance.ingredients)
            if nutrition_data:
                instance.nutrition_data = nutrition_data
                instance.save()
                return redirect('recipe_detail', recipe_id=instance.id)
            else:
                form.add_error(None, "no data added")

    else:
        form = RecipeNutritionForm()
    return render(request, 'NutritionApi/recipe_form.html', {'form': form})


def recipe_detail(request, recipe_id):
    recipe = RecipeNutrition.objects.get(id=recipe_id)
    return render(request, 'NutritionApi/recipe_detail.html', {'recipe': recipe})
