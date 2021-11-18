from csv import writer
from Classes.users import Ciudadano, Usuario
from admin_menu import AdminMenu, menu_admin
import folium
import pandas
import webbrowser

class Start:
    def checkCuil(self):
        check = False
        while check == False:
            cuil = input('Please enter your CUIL: ')
            try:
                #falta que chequee el anses database
                with open('Datasets\\User_database.csv', 'r') as user_database:
                    for i in user_database:
                        row = i.strip().split(',')
                        if cuil == row[0]:
                            print ("Cuil already exist, try another one")
                            raise ValueError
                check = True
                return cuil

            except ValueError:
                pass



    def checkPhoneNumber(self):                                
        check = False
        while check == False:
            try:
                with open('Datasets\\User_database.csv', 'r') as user_database:
                    phone_number = input('Please enter your phone number: ')    
                    for line in user_database:
                        row = line.strip().split(',')
                        if phone_number == row[1].strip():
                            print ("phone number already exist, try another one")
                            raise ValueError
                        else: 
                            check = True
                            return phone_number
            except ValueError:
                pass
                    

    def checkUsername(self):     
        check = False
        while check == False:
            try:
                with open('Datasets\\User_database.csv', 'r') as user_database:
                        username = input('Enter your username: ')
                        for line in user_database:
                            row = line.strip().split(',')
                            if username == row[2].strip():
                                print ("Username already exist, try another one")
                                raise ValueError
                            else: 
                                check = True
                                return username
            except ValueError:
                pass

    def checkPassword(self):
        check = False
        while check == False:
            password = input('Enter your password: ')
            confirm_password = input('Please re-enter your password:')
            if password != confirm_password:
                print('Passwords do not match, please try again.')
                Start.checkPassword(self)
            else: 
                check = True
                return password
                
    def Register(self):
        cuil = Start.checkCuil(self)
        phone_number = Start.checkPhoneNumber(self)
        username = Start.checkUsername(self)
        password = Start.checkPassword(self) 
        with open('Datasets\\User_database.csv', 'a', newline='') as user_database:
            user = Ciudadano(username, password, cuil, phone_number) #para poder acceder a notifs, funciones, etc
            user_data = [cuil, phone_number, user.username, user.password]
            data_writer = writer(user_database, lineterminator='\r')
            data_writer.writerow(user_data)
        with open(f'Users\\{cuil}.csv', 'w', newline = '') as user_csv:
            user_writer = writer(user_csv, lineterminator = '\r')
            user_writer.writerow(user_data)
            friend_list = ['Friends']
            user_writer.writerow(friend_list)

    def Login(self):
        log = False
        while not log:
            username = input('Enter Username: ').rstrip()
            password = input('Enter Password: ')
            with open('Datasets\\User_database.csv', 'r') as database:
                try:
                    for line in database:
                        row = line.strip().split(',')
                        if username == row[2].strip():
                                if password == row[3].strip():
                                    cuil = row[0]
                                    with open(f'Users\\{cuil}.csv', 'r') as user_data:
                                        copied_data = list()
                                        for line in user_data:
                                            row = line.strip().split(',')
                                            copied_data.append(row)
                                    with open('Datasets\\CurrentUser.csv', 'w') as user:
                                        data_writer = writer(user, lineterminator = '\r')
                                        for data in copied_data:    
                                            data_writer.writerow(data)
                                    log = True
                                    #algo que te mande a interfaz
                    if log:
                        pass
                    else:
                        raise ValueError
                except ValueError:
                    print('Username and password do not match. Please try again.')
                    pass

    def LoginAdmin(self):
        log = False
        while not log:
            username = input('Enter username: ').rstrip()
            password = input('Enter password: ')
            with open('Datasets\\Admin_dataset.csv', 'r') as database:
                try:
                    for line in database:
                        row = line.strip().split(',')
                        if username == row[0].strip():
                            if password == row[1].strip():
                                menu_admin.Admin_mainMenu()
                                log = True
                                #algo que te mande a interfaz admin
                    if not log:
                        raise ValueError
                except ValueError:
                    print('Username and password do not match. Please try again.')


    def LoginSensor(self):
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

            folium.Marker(location=[marker_csv.iloc[i]['$$_lat_$$'], marker_csv.iloc[i]['$$_long_$$']], popup=popup2).add_to(mapa)

        mapa.save('mapa.html')
        webbrowser.open('mapa.html')
menuLogin = Start()
