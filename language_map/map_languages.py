import folium
import sys 

file = open("query.tsv", 'r+')
file.readline()
data, latlongs = [], []
for line in file:
    line = line[:-1]
    row = line.split('\t')
    if row[-1] == "":
        latlong = [-16.9, -87.5]
    else:
        latlong = list(map(float, row[-1].split()))

    data.append(row)
    latlongs.append(latlong)

# Map!
world_map = folium.Map(tiles="OpenStreetMap")

for ll, x in zip(latlongs, data):
    lat, long = ll
    folium.CircleMarker(location = [lat, long], tooltip=f'Language: {x[1]}', radius=5, fill=True).add_to(world_map)

world_map.save(sys.argv[1])
