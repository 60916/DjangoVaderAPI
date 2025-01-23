import requests
from django.http import JsonResponse

def get_weather_data(request):
    # Example coordinates for Berlin, Germany
    latitude = request.GET.get('latitude', '52.52')
    longitude = request.GET.get('longitude', '13.41')
    api_url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code,pressure_msl",
        "timezone": "auto",
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.RequestException as e:
        return JsonResponse({"error": "Unable to fetch weather data", "details": str(e)}, status=500)
