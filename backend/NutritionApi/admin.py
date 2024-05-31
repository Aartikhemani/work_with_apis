from django.contrib import admin
from .models import RecipeNutrition
from .views import get_nutrition_facts


@admin.register(RecipeNutrition)
class RecipeNutritionAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingredients', 'instructions', 'nutrition_data')
    readonly_fields = ('nutrition_data',)

    def save_model(self, request, obj, form, change):
        if not change:  # Only fetch nutrition data when creating a new object
            obj.nutrition_data = get_nutrition_facts(obj.ingredients)
        super().save_model(request, obj, form, change)
