import requests

# This module provides a WeatherForecastTool class to fetch current weather and 
# weather forecasts for a given place using the OpenWeatherMap API.

class WeatherForecastTool:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    # Fetches the current weather for the specified place.
    # Builds the request URL and parameters.
    # Returns the JSON response if successful, otherwise returns an empty dictionary.
    def get_current_weather(self, place:str):
        """Get current weather of a place"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
    # Fetches the weather forecast for the specified place.
    # Requests 10 forecast data points in metric units.
    # Returns the JSON response if successful, otherwise returns an empty dictionary.
    def get_forecast_weather(self, place:str):
        """Get weather forecast of a place"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": place,
                "appid": self.api_key,
                "cnt": 10,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e