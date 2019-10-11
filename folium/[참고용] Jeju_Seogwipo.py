import os
# import sys
import requests
import json
# import mariadbfunc3 as db
import folium
import numpy as np
import pandas as pd
import webbrowser



map_osm = folium.Map(location=[33.5779071,126.2921622], zoom_start=10, tiles='Stamen Toner')
rfile = open('D:/ai/pythonP/basic/crawling/folium_test/skorea-municipalities-2018-geo.json', 'r', encoding='utf-8').read()
jsonData = json.loads(rfile)

jsonData_jeju = {"type": "FeatureCollection"}
jsonData_jeju_list = []

for idx in jsonData["features"]:
    idx['index']=idx["properties"]["name"]
    # count = 1
    if idx['index'] == "제주시" or idx["index"] == "서귀포시":
        jsonData_jeju_list.append(idx)
        pass
    # else:
    #     del jsonData[]

jsonData_jeju['features'] = jsonData_jeju_list
print(jsonData_jeju)
folium.GeoJson(jsonData_jeju, name='json_data').add_to(map_osm)
svFileName = 'geo2.html'
map_osm.save('D:/ai/pythonP/basic/crawling/folium_test/'+svFileName)
webbrowser.open('D:/ai/pythonP/basic/crawling/folium_test/'+svFileName)

