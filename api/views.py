from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantCreateUpdateSerializer, RestaurantDetailSerializer

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

# Complete me
class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field= "id"
	lookup_url_kwarg = 'restaurant_id'



# Complete me
class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer
	lookup_field= "id"
	lookup_url_kwarg = 'restaurant_id'





# Complete me
class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	lookup_field= "id"
	lookup_url_kwarg = 'restaurant_id'

