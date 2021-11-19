import folium, pandas, webbrowser

def enter_map():
    mapaBsAs = folium.Map(location=[-36.233913, -60.645759], zoom_start=7)
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
        
        
        folium.Marker(location= [marker_csv.iloc[i]['$$_lat_$$'], marker_csv.iloc[i]['$$_long_$$']], popup= popup2).add_to(mapaBsAs)

    mapaBsAs.save('mapa.html')
    webbrowser.open('mapa.html')

def seleccionarZona():
    with open('Datasets\\Zone_markers.csv', 'r', newline='') as tipos:
        i = 0
        for line in tipos:
            if i != 0:
                row = line.strip().split(",")
                print(f"{i}. {row[0]}")
            i += 1
    try:
        with open('Datasets\\Zone_markers.csv', 'r', newline='') as tipos: 
            seleccion = input("\nNúmero de la zona que quiere elegir: ")
            sel = int(seleccion)
            stop = 0
            for line in tipos:
                row = line.strip().split(",")
                if stop == sel:
                    return row[0]
                stop += 1
    except:
        print("debe ingresar un número que este dentro del rango")
        seleccionarZona()


# class mapa:
#     #algun tipo de grid o matriz con coordenadas
#     pass

# class zona:
#     #cada zona es tiene sus propias coordenadas en el mapa
#     pass
