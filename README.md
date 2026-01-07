# Weather Explainer

A Django web application that explains weather data in an easy-to-understand format. Search for any city worldwide and get current weather information with detailed explanations of each metric.

## Features

- 🌍 Search weather for any city worldwide
- 🌡️ View temperature, humidity, wind speed, and more
- 📚 Educational explanations of weather metrics
- 🎨 Beautiful, responsive UI
- 🔄 Real-time weather data from OpenWeatherMap API

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository
```bash
git clone https://github.com/eleanorjboyd/testing-website.git
cd testing-website
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` and add your OpenWeatherMap API key (get one free at https://openweathermap.org/api)

5. Run database migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

7. Open your browser and visit `http://127.0.0.1:8000/`

## Usage

1. Enter a city name in the search box (e.g., "London", "Tokyo", "New York")
2. Click "Get Weather" to fetch current weather data
3. View the temperature, conditions, and detailed weather metrics
4. Read the explanations below to understand what each metric means

## API Key Setup

This application uses the OpenWeatherMap API. To get your free API key:

1. Visit https://openweathermap.org/api
2. Sign up for a free account
3. Navigate to API Keys section
4. Copy your API key
5. Add it to your `.env` file: `WEATHER_API_KEY=your-key-here`

## Technologies Used

- Django 4.2
- OpenWeatherMap API
- HTML/CSS
- Python requests library