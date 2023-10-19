#!/usr/bin/env python
# coding: utf-8

# ## Récolte des données météorologiques

# In[1]:


import requests

def get_weather(city):
    response = requests.get(f'http://api.weatherstack.com/current?access_key=c2591c1b872564a6299d9c0ed03475bd&query={city}')
    return response.json()

# Utilisez la fonction pour obtenir la météo pour une ville spécifique
weather_data = get_weather('Montpellier')
print(weather_data)


# In[ ]:




