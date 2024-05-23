from django.urls import path
from .views import NearbyRestaurantsView, restaurant_form_view

urlpatterns = [

        path('api/nearby_restaurants/', NearbyRestaurantsView.as_view(), name='nearby_restaurants'),
        path('restaurant_form_view/', restaurant_form_view, name='restaurant_form'),
]