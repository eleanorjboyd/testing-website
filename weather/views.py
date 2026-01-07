from django.shortcuts import render
from django.conf import settings
import requests


def index(request):
    """Home page with weather information."""
    return render(request, 'weather/index.html')


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
    
    context = {
        'city': city,
        'weather_data': weather_data,
        'error': error,
    }
    
    return render(request, 'weather/index.html', context)
