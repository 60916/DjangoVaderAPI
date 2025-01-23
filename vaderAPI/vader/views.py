import requests
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Berlin"
    response = requests.get(url)
    return response.json()

def get_weather_forecast(request):
    data = fetch_weather_data()
    return JsonResponse(data)

def get_monthly_averages(request):
    data = fetch_weather_data()
    monthly_averages = {}
    for i, day in enumerate(data['daily']['time']):
        date = datetime.strptime(day, '%Y-%m-%d')
        month = date.strftime('%B')
        if month not in monthly_averages:
            monthly_averages[month] = {'temperature_sum': 0, 'days_count': 0}
        daily_temp = (data['daily']['temperature_2m_max'][i] + data['daily']['temperature_2m_min'][i]) / 2
        monthly_averages[month]['temperature_sum'] += daily_temp
        monthly_averages[month]['days_count'] += 1
    for month in monthly_averages:
        monthly_averages[month]['average_temperature'] = monthly_averages[month]['temperature_sum'] / monthly_averages[month]['days_count']
    return JsonResponse(monthly_averages)
