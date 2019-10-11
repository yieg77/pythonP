import os
# import sys
import requests
import json
# import mariadbfunc3 as db
import folium
import numpy as np
import pandas as pd
import webbrowser

jeju_dong = ['일도1동','일도2동','이도1동','이도2동','삼도1동','삼도2동','용담1동','용담2동','건입동','화북동','삼양동','봉개동','아라동','오라동','연동','노형동','외도동','이호동','도두동']
jeju = ['제주','애월읍','조천읍','구좌읍','한림읍','한경면','추자면']
seogwi_dong = ['송산동','정방동','천지동','효돈동','영천동','동홍동','서홍동','대륜동','대천동','중문동','예래동']
seogwi = ['서귀포','안덕면','대정읍','남원읍','표선면','성산읍','우도면']

jeju = jeju + jeju_dong
seogwi = seogwi + seogwi_dong
jejudo = jeju  + seogwi

map_osm = folium.Map(location=[33.5779071,126.2921622], zoom_start=10, tiles='Stamen Toner')
rfile = open('D:/ai/pythonP/basic/crawling/folium_test/skorea-submunicipalities-2018-geo.json', 'r', encoding='utf-8').read()
jsonData = json.loads(rfile)

jsonData_jeju = {"type": "FeatureCollection"}
jsonData_jeju_list = []

for idx in jsonData["features"]:
    idx['id']=idx["properties"]["name"]
    # count = 1

    for idx2 in jejudo:
        if idx['id'] == idx2:
            jsonData_jeju_list.append(idx)
            pass
    # else:
    #     del jsonData[]

jsonData_jeju['features'] = jsonData_jeju_list
print(jsonData_jeju)
folium.GeoJson(jsonData_jeju, name='json_data').add_to(map_osm)
svFileName = 'geo3.html'
map_osm.save('D:/ai/pythonP/basic/crawling/folium_test/'+svFileName)
webbrowser.open('D:/ai/pythonP/basic/crawling/folium_test/'+svFileName)

