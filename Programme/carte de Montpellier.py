import pandas as pd 
import matplotlib.pyplot as plt
import folium
import numpy
import geopandas as gpd
import folium

meteo_data = r'C:\Users\BossdiDibosS\Desktop\open-meteo-43.58N3.96E4m.csv'

# On lis chaque section du fichier séparément
df1 = pd.read_csv(r'C:\Users\BossdiDibosS\Desktop\open-meteo-43.58N3.96E4m.csv', skiprows=0, nrows=4)
df2 = pd.read_csv(r'C:\Users\BossdiDibosS\Desktop\open-meteo-43.58N3.96E4m.csv', skiprows=5, nrows=685, error_bad_lines=False)
df3 = pd.read_csv(r'C:\Users\BossdiDibosS\Desktop\open-meteo-43.58N3.96E4m.csv', skiprows=list(range(685)))

# On fusionne les DataFrames
df = pd.concat([df1, df2, df3])

#affichage des premières lignes du dataframe
df.head()

# Création d'une carte centrée sur Montpellier
carte = folium.Map(location=[43.61, 3.88], zoom_start=10)

df.columns = df.columns.str.strip() 

for _, r in df.iterrows():
    # Créeation d'un marqueur pour chaque point de données
    folium.Marker(
        location=[r['latitude'], r['longitude']],
        popup=f"time : {r['time']}<br>"
              f"temperature_2m (°C): {r['temperature_2m (°C)']}°C<br>"
              f"temperature_2m_max (°C): {r['temperature_2m_max (°C)']}°C<br>"
              f"temperature_2m_min (°C): {r['temperature_2m_min (°C)']}°C<br>"
              f"relativehumidity_2m (%) : {r['relativehumidity_2m (%)']}%<br>"
              f"apparent_temperature (°C): {r['apparent_temperature (°C)']}°C<br>"
    ).add_to(carte)
carte

# Enregistrement de la carte en tant que fichier HTML
carte.save("carte_meteo.html")





