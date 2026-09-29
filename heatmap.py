import pgeocode
import pandas as pd
import folium
from folium.plugins import HeatMap

nomi = pgeocode.Nominatim('fr')
print(nomi.query_postal_code("75013"))

df = pd.DataFrame({
"lat": [52.23, 50.06, 54.35],
"lon": [21.01, 19.94, 18.65],
"value": [100, 50, 20]
})

m = folium.Map(
    location=[52.0, 19.0],
    zoom_start=6,
    tiles="OpenStreetMap"
)

folium.TileLayer(
tiles="https://tile.openstreetmap.de/{z}/{x}/{y}.png",
attr="OpenStreetMap"
).add_to(m)

heat_data = [
    [row["lat"], row["lon"], row["value"]]
    for _, row in df.iterrows()
]

HeatMap(
    heat_data,
    radius=20,
    blur=15,
    max_zoom=10
).add_to(m)

m.save("polska_heatmap.html")