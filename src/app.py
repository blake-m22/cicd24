"""
    Easy Azure Streamlit Demo
    Blake Moore
"""
import streamlit as st
import requests
from log import logger

def fetch_weather_data(city: str, api_key: str) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to fetch weather data for {city}.")
        return {}

def ui(weather_data: dict) -> None:
    if weather_data:
        st.title("Weather Forecast")
        st.subheader(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Description: {weather_data['weather'][0]['description'].capitalize()}")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.error("Failed to fetch weather data. Please try again later.")

if __name__ == "__main__":
    city = st.text_input("Enter city name:")
    api_key = "5536458d16fb34c0a634ea3edfcaef99"

    if city:
        weather_data = fetch_weather_data(city, api_key)
        ui(weather_data)
