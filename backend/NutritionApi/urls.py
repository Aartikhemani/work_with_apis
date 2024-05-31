from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, recipe_form, recipe_detail, home

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('nutrition_facts/', include(router.urls)),
    path('recipe_form/', recipe_form, name='recipe_form'),  # Add new recipe form URL
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]
