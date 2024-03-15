import requests
import os
from dotenv import load_dotenv
import streamlit as st


# Choix des villes
CHOICE_CITY = [
    "Los Angeles",
    "San Diego",
    "San Jose",
    "San Francisco",
    "Sacramento",
    "Fresno",
    "Long Beach",
    "Oakland",
    "Bakersfield",
    "Anaheim",
    "Santa Ana",
    "Riverside",
    "Stockton",
    "Irvine",
    "Chula Vista",
]

def fetch_data_city_locality(city):
    load_dotenv('.env')
    key=os.environ['KEY']
    URL = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        longitude = data[0]["lat"]
        latitude  = data[0]["lon"] 
        return longitude, latitude
    else:
        return st.error("ERROR !")