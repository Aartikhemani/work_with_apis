from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import googlemaps
from django.conf import settings
from .serializers import RestaurantSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'NearRestApi/home.html')


class NearbyRestaurantsView(APIView):
    def get(self, request):
        try:
            # Retrieve query parameters
            place_name = request.query_params.get('place_name')
            cuisine_type = request.query_params.get('cuisine_type')

            # Validate input parameters
            if not place_name:
                return Response({"error": "Please provide a place name"}, status=status.HTTP_400_BAD_REQUEST)

            # Initialize Google Maps client
            gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)

            # Use Geocoding API to get latitude and longitude for the place name
            geocode_result = gmaps.geocode(place_name)
            if not geocode_result:
                return Response({"error": "Could not geocode the provided place name"},
                                status=status.HTTP_400_BAD_REQUEST)

            location = geocode_result[0]['geometry'][
                'location']  # retrieves the location information including latitude and longitude.
            latitude = location['lat']  # extracts the latitude value.
            longitude = location['lng']  # extracts the longitude value.

            # Fetch nearby places using latitude and longitude
            places = gmaps.places_nearby(location=(latitude, longitude), radius=5000, type='restaurant',
                                         keyword=cuisine_type)

            # Serialize data
            restaurants = []
            for place in places['results']:
                serializer = RestaurantSerializer(data=place)
                if serializer.is_valid():
                    restaurants.append(serializer.data)

            return Response(restaurants, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def restaurant_form_view(request):
    return render(request, 'NearRestApi/near_rest.html')
