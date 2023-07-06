import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv('tripdata_01.csv')

class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    
    def gen_map(self):
        mp = folium.Map(location=self.center, zoom_start=11)
        mp.add_child(HeatMap(df[['pickup_latitude', 'pickup_longitude']].values.tolist(), radius=15))
        mp.save("HeatMap-Pickup.html")
        del mp
        md = folium.Map(location=self.center, zoom_start=11)
        md.add_child(HeatMap(df[['dropoff_latitude', 'dropoff_longitude']].values.tolist(), radius=15))
        md.save("HeatMap-Dropoff.html")
        del md
        ma = folium.Map(location=self.center, zoom_start=11)
        ma.add_child(HeatMap(df[['pickup_latitude', 'pickup_longitude']].values.tolist(), radius=15))
        ma.add_child(HeatMap(df[['dropoff_latitude', 'dropoff_longitude']].values.tolist(), radius=15))
        ma.save("HeatMap-PickupDropoff.html")
        del ma

#Define coordinates of where we want to center our map
coords = [40.730610,-73.935242]
map = Map(center = coords, zoom_start = 11)
map.gen_map()
