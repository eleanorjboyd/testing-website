from django.shortcuts import render
from django.conf import settings
import requests


def index(request):
    """Home page with weather information."""
    top_cities = [
        'London', 'New York', 'Tokyo', 'Paris', 'Sydney', 'Moscow', 'Rio de Janeiro',
        'Cape Town', 'Toronto', 'Beijing', 'Dubai', 'Berlin', 'Rome', 'Bangkok', 'Istanbul'
    ]
    return render(request, 'weather/index.html', {'top_cities': top_cities})

import random

def about(request):
    return render(request, 'weather/about.html')

def random_weather(request):
    """Show weather for a random city."""
    cities = [
        'London', 'New York', 'Tokyo', 'Paris', 'Sydney', 'Moscow', 'Rio de Janeiro',
        'Cape Town', 'Toronto', 'Beijing', 'Dubai', 'Berlin', 'Rome', 'Bangkok', 'Istanbul'
    ]
    city = random.choice(cities)
    weather_data = None
    error = None
    api_key = settings.WEATHER_API_KEY
    if api_key:
        try:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                alerts = data.get('alerts', [])
                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': round(data['main']['temp']),
                    'feels_like': round(data['main']['feels_like']),
                    'description': data['weather'][0]['description'].capitalize(),
                    'humidity': data['main']['humidity'],
                    'wind_speed': round(data['wind']['speed'] * 3.6, 1),
                    'icon': data['weather'][0]['icon'],
                    'alerts': alerts,
                }
            else:
                error = f"City '{city}' not found. Please try another city."
        except requests.exceptions.RequestException:
            error = "Unable to fetch weather data. Please try again later."
    else:
        error = "Weather API key not configured. Please add WEATHER_API_KEY to .env file."
    context = {
        'city': city,
        'weather_data': weather_data,
        'error': error,
        'random': True,
    }
    return render(request, 'weather/index.html', context)


def search_weather(request):
    """Search for weather by city name."""
    city = request.GET.get('city', '')
    weather_data = None
    error = None
    
    if city:
        # Using OpenWeatherMap API (free tier)
        api_key = settings.WEATHER_API_KEY
        
        if api_key:
            try:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        'city': data['name'],
                        'country': data['sys']['country'],
                        'temperature': round(data['main']['temp']),
                        'feels_like': round(data['main']['feels_like']),
                        'description': data['weather'][0]['description'].capitalize(),
                        'humidity': data['main']['humidity'],
                        'wind_speed': round(data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                        'icon': data['weather'][0]['icon'],
                    }
                else:
                    error = f"City '{city}' not found. Please try another city."
            except requests.exceptions.RequestException:
                error = "Unable to fetch weather data. Please try again later."
        else:
            error = "Weather API key not configured. Please add WEATHER_API_KEY to .env file."
    
    top_cities = [
        'London', 'New York', 'Tokyo', 'Paris', 'Sydney', 'Moscow', 'Rio de Janeiro',
        'Cape Town', 'Toronto', 'Beijing', 'Dubai', 'Berlin', 'Rome', 'Bangkok', 'Istanbul'
    ]
    # Nearby cities using OpenWeatherMap 'find' endpoint
    nearby_cities = []
    if weather_data:
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        try:
            find_url = f'https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=5&appid={api_key}&units=metric'
            find_resp = requests.get(find_url, timeout=10)
            if find_resp.status_code == 200:
                find_data = find_resp.json()
                for city_info in find_data.get('list', []):
                    if city_info['name'].lower() != city.lower():
                        nearby_cities.append({
                            'name': city_info['name'],
                            'country': city_info['sys']['country'],
                            'temperature': round(city_info['main']['temp']),
                        })
        except Exception:
            pass
    context = {
        'city': city,
        'weather_data': weather_data,
        'error': error,
        'top_cities': top_cities,
        'nearby_cities': nearby_cities,
    }
    
    return render(request, 'weather/index.html', context)
