from csv import writer
from Classes.users import Ciudadano, Usuario
from admin_menu import AdminMenu, menu_admin

class Start:
    def checkCuil(self):
        check = False
        while check == False:
            cuil = input('Please enter your CUIL: ')
            with open('Datasets\\dataset_Anses.csv', 'r') as anses_database:
                try:
                    for line in anses_database:
                        if line == cuil:
                            with open('Datasets\\User_database.csv', 'r') as user_database:
                                    for i in user_database:
                                        row = i.strip().split(',')
                                        if cuil == row[0].strip():
                                            print ("Cuil already exist, try another one")
                                            raise ValueError
                                        else: 
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
            user_data = [cuil, phone_number, user.username, user.password, user]
            data_writer = writer(user_database, lineterminator='\r')
            data_writer.writerow(user_data)

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
                                    with open('Datasets\\CurrentUser.csv', 'w') as user:
                                        data_writer = writer(user, lineterminator = '\r')
                                        data_writer.writerow(row)
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
        log = False #SE PUEDE CAMBIAR PARA MANDAR DIRECTO AL MAPA, VA A SER MUCHO MEJOR
        while not log:
            username = input('Enter Area Code: ').rstrip()
            with open('Datasets\\User_database.csv', 'r') as database:
                try:
                    for line in database:
                        row = line.strip().split(',')
                        if username == row[0].strip():
                            log = True
                except:
                    print("Area no disponible")
