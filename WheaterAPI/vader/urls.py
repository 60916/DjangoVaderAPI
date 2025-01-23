from django.urls import path
from .views import get_weather_data

urlpatterns = [
    path('api/WheaterAPI/', get_weather_data, name='get_weather_data'),
]
