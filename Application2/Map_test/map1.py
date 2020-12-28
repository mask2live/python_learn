import folium

my_addr = folium.Map(
    location=[22.55, 114.026], 
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}', 
    attr='default'
)

my_addr.save('my_addr.html')