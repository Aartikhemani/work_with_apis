from django import forms
from .models import RecipeNutrition


class RecipeNutritionForm(forms.ModelForm):
    class Meta:
        model = RecipeNutrition
        fields = ['title', 'ingredients', 'instructions']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 10, 'cols':30}),
            'instructions': forms.Textarea(attrs={'rows': 10, 'cols':30})
        }
