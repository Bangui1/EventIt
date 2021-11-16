import folium, pandas, webbrowser

mapa = folium.Map(location=[-36.233913, -60.645759], zoom_start=7)
    
    
marker_csv = pandas.read_csv('Datasets\Zone_markers.csv')
for i in range(0, len(marker_csv)):
    folium.Marker(location= [marker_csv.iloc[i]['lat'], marker_csv.iloc[i]['lng']], popup= marker_csv.iloc[i]['Nombre']).add_to(mapa)

mapa.save('mapa.html')
webbrowser.open('mapa.html')




# class mapa:
#     #algun tipo de grid o matriz con coordenadas
#     pass

# class zona:
#     #cada zona es tiene sus propias coordenadas en el mapa
#     pass
