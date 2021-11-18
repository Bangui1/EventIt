import folium, pandas, webbrowser

mapa = folium.Map(location=[-36.233913, -60.645759], zoom_start=7)
    
marker_csv = pandas.read_csv('Datasets\Zone_markers.csv')



for i in range(0, len(marker_csv)):
    def info():
        with open('Datasets\\Events_database.csv', 'r') as events:
            info = ""
            for line in events:
                row = line.strip().split(",")
                if marker_csv.iloc[i]['$$_Nombre_$$'].strip() == row[1].strip():
                    info += f"Tipo: {row[0]}, {row[2]}, personas: {len(row) - 3} \n"
            return info
    
    popup_info = info()
    iframe = folium.IFrame(popup_info, width=350, height=100)
    popup2 = folium.Popup(iframe)
    
    
    folium.Marker(location= [marker_csv.iloc[i]['$$_lat_$$'], marker_csv.iloc[i]['$$_long_$$']], popup= popup2).add_to(mapa)

mapa.save('mapa.html')
webbrowser.open('mapa.html')




# class mapa:
#     #algun tipo de grid o matriz con coordenadas
#     pass

# class zona:
#     #cada zona es tiene sus propias coordenadas en el mapa
#     pass
