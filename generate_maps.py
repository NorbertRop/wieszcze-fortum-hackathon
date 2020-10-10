
import folium
from folium import plugins
import pandas as pd
import numpy as np

gradient_default = {0.4: 'blue', 0.65: 'lime', 1: 'red'}
radius = 20
blur = 40

df = pd.read_json('data/data_without_date.json').head(10000)

m_energy = folium.Map(location=[51.1113305, 17.041928], zoom_start=14)

en_minus = df[df['energy_delta'] < 0][['x', 'y', 'energy_delta']]
en_minus['energy_delta'] = en_minus.energy_delta.apply(np.abs)

locations_minus = en_minus.to_numpy()
gradient_minus = {0.4: 'yellow', 0.65: 'orange', 1: 'red'}
m_energy.add_child(plugins.HeatMap(locations_minus, name='excess energy', radius=radius, blur=blur, gradient=gradient_minus))

locations_plus = df[df['energy_delta'] > 0][['x', 'y', 'energy_delta']].to_numpy()
gradient_plus = {0.4: 'lightblue', 0.65: 'blue', 1: 'darkblue'}
m_energy.add_child(plugins.HeatMap(locations_plus, name='energy consumption', radius=radius, blur=blur, gradient=gradient_plus))

folium.LayerControl().add_to(m_energy)
m_energy.save('map_energy.html')
print('map_energy done :D')

population = df[['x', 'y', 'population']].to_numpy()
m_pop = folium.Map(location=[51.1113305, 17.041928], zoom_start=15)
m_pop.add_child(plugins.HeatMap(population, radius=radius, blur=blur, gradient=gradient_minus))
m_pop.save('map_population.html')
print('map_population done :D')

traffic = df[['x', 'y', 'traffic']].to_numpy()
gradient = {0.4: 'white', 0.8: 'orange', 1: 'red'}
m_traffic = folium.Map(location=[51.1113305, 17.041928], zoom_start=14)
m_traffic.add_child(plugins.HeatMap(traffic, radius=radius, blur=blur, gradient=gradient))
m_traffic.save('map_traffic.html')
print('map_traffic done :D')

