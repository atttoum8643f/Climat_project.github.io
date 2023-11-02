#!/usr/bin/env python
# coding: utf-8

# # Données météorologique 

# In[25]:


#sourrce du code:"weatherstack"


# In[26]:


import requests
import datetime

def get_weather(api_key, location):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": location
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    current = data['current']
    location = data['location']['name']
    weather_icon = current['weather_icons'][0]
    temperature = current['temperature']
    localtime = data['location']['localtime']
    weather_description = current['weather_descriptions'][0]

    print(f"Location: {location}")
    print(f"Weather Icon URL: {weather_icon}")
    print(f"Temperature: {temperature}°C")
    print(f"Local Time: {localtime}")
    print(f"Weather Description: {weather_description}")

api_key = "votre_clef_API"
location = "Montpellier"
data = get_weather(api_key, location)
display_weather(data)


# In[30]:


#Utilisation d'une clef API de Open météo


# In[ ]:


import requests
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium

# Remplacez "VOTRE_CLE_API" par votre clé API OpenMeteo
api_key = "https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation&daily=temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=16"

# Utilisez l'API OpenMeteo pour récupérer les données météorologiques
url = f"https://api.open-meteo.com/v1/forecast?latitude=43.6109&longitude=3.8763&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation&daily=temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=16"
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
data = response.json()

# Créez un DataFrame Pandas pour les données actuelles
current_data = data["current"]
current_df = pd.DataFrame(current_data, index=["Actuel"])

# Créez un DataFrame Pandas pour les données horaires
hourly_data = data["hourly"]
hourly_df = pd.DataFrame(hourly_data)

# Créez un DataFrame Pandas pour les données quotidiennes
daily_data = data["daily"]
daily_df = pd.DataFrame(daily_data)

# Affichez les données météorologiques
print("Données météorologiques actuelles :")
print(current_df)
print("\nDonnées météorologiques horaires :")
print(hourly_df)
print("\nDonnées météorologiques quotidiennes :")
print(daily_df)

# Créez un graphique pour afficher les données
plt.figure(figsize=(10, 6))
plt.plot(hourly_df.index, hourly_df["temperature_2m"], label="Température (°C)")
plt.plot(hourly_df.index, hourly_df["precipitation"], label="Précipitations (mm)")
plt.xlabel("Heure")
plt.ylabel("Valeurs")
plt.title("Évolution de la température et des précipitations")
plt.legend()
plt.grid()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




