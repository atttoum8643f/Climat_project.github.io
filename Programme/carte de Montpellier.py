
# # Carte interractive de Montpellier

# In[3]:


import folium

# Créer une carte centrée sur Montpellier
c = folium.Map(location=[43.61, 3.88], zoom_start=10)

# Ajout de marqueur pour Montpellier
folium.Marker([43.61, 3.88], popup='Montpellier').add_to(c)

# Afficher la carte
c


c.save('Montpellier_map.html')





