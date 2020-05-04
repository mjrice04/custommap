# import folium package
import folium
from address_input import lat_long_data_handler

my_map = folium.Map(location=[42.3465694,-71.0987712],
                     zoom_start=15)

address_csv = lat_long_data_handler()


for index, row in address_csv.iterrows():
    lat = row['LAT']
    lng = row['LNG']
    comment = row['Comment']
    # Pass a string in popup parameter
    folium.Marker([lat, lng],
                  popup=folium.Popup(comment, max_width=450)).add_to(
        my_map)

my_map.save("output/custom_map_example.html")
