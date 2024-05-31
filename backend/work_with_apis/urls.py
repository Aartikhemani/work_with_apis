from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from NutritionApi.views import RecipeViewSet
from MainApp import views as MainAppViews
# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', MainAppViews.home, name='home'),
    path('admin/', admin.site.urls),
    path('NearRestApi/', include('NearRestApi.urls')),
    path('NutritionApi/', include('NutritionApi.urls')),
    path('nutrition_facts/', include(router.urls)),
    # Include the router URLs
]
