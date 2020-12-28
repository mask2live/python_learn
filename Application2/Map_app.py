import folium
import pandas
import json


# choose a color by value of the specified element 
def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


# create a marker by location, volcanoes height and a panel to inform
def normal_marker_producer(lat, lon, elev, iframe):
    return folium.Marker(
            location=[lat, lon], 
            popup=folium.Popup(iframe), 
            icon=folium.Icon(color=color_producer(elev))
    )


# create a circle marker other things are same as above        
def circle_marker_producer(lat, lon, elev, iframe):
    return folium.CircleMarker(
        location=[lat, lon],
        popup=folium.Popup(iframe),
        fill_color=color_producer(elev),
        fill_opacity=0.8,
        color='white'
    )


# extract data from specified file
def get_data(file_path):
    data = pandas.read_csv(file_path)
    location_data = zip(
        data['LAT'], 
        data['LON'], 
        data['NAME'], 
        data['LOCATION'],
        data['ELEV']
        )
    return location_data


# create a panel to inform the details of volcanoes
def panel_producer(name, loc, elev):

    html = """<h4>Volcano information:</h4>
    location:%s %s
    Height:%s m

    """

    return folium.IFrame(
            html=html % (name, loc, elev), 
            width=200, 
            height=100)


# built two function maps in one real map
# one is display volcanoes information
# other is display population of countries
def app2():
    map = folium.Map(zoom_start=15)

    location_data = get_data('Application2/Volcanoes.txt')

    #
    fgroupV = folium.FeatureGroup('Volcanoes')

    for lat, lon, name, loc, elev in location_data:
        iframe = panel_producer(name, loc, elev)
        fgroupV.add_child(circle_marker_producer(lat, lon, elev, iframe))

    fgroupP = folium.FeatureGroup('Population')

    fgroupP.add_child(folium.GeoJson(
        data=json.load(open('Application2/world.json', 'r', encoding = 'utf-8-sig')), 
        style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000 else 'red'})
    )

    map.add_child(fgroupP)
    map.add_child(fgroupV)
    map.add_child(folium.LayerControl())

    map.save('Map.html')


if __name__ == '__main__':

    app2()