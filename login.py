from csv import writer
from Classes.users import Ciudadano, Usuario

class Start:
        
    def checkCuil(self):
        with open('EventIt\\Datasets\\User_database.csv', 'r') as user_database:
            check_1 = False
            while check_1 == False:
                cuil = input('Please enter your CUIL: ')
                for i in user_database:
                    row = i.strip().split(',')
                    if cuil == row[0].strip():
                        print ("Cuil already exist, try another one")
                        Start.checkCuil(self)
                    else: 
                        check_1 = True
                        return cuil

    def checkPhoneNumber(self):                                
        with open('EventIt\\Datasets\\User_database.csv', 'r') as user_database:
            check_2 = False
            while check_2 == False:
                phone_number = input('Please enter your phone number: ')    
                for x in user_database:
                    row = x.strip().split(',')
                    if phone_number == row[1].strip():
                        print ("phone number already exist, try another one")
                        Start.checkPhoneNumber(self)
                    else: 
                        check_2 = True
                        return phone_number
                    

    def checkUsername(self):     
        with open('EventIt\\Datasets\\User_database.csv', 'r') as user_database:
            check_3 = False
            while check_3 == False:
                username = input('Enter your username: ')
                for y in user_database:
                    row = y.strip().split(',')
                    if username == row[2].strip():
                        print ("Username already exist, try another one")
                        Start.checkUsername(self)
                    else: 
                        check_3 = True
                        return username
                    

    def checkPassword(self):      
        check_4 = False
        while check_4 == False:
            password = input('Enter your password: ')
            confirm_password = input('Please re-enter your password:')
            if password != confirm_password:
                print('Passwords do not match, please try again.')
                Start.checkPassword(self)
            else: 
                check_4 = True
                return password
                
    def Register(self):
        cuil = Start.checkCuil(self)
        phone_number = Start.checkPhoneNumber(self)
        username = Start.checkUsername(self)
        password = Start.checkPassword(self) 
        cuil
        phone_number
        username
        password
        with open('EventIt\\Datasets\\User_database.csv', 'a', newline='') as user_database:
            user = Ciudadano(username, password, cuil, phone_number) #para poder acceder a notifs, funciones, etc
            user_data = [user.cuil, user.phone_number, user.username, user.password, user]
            data_writer = writer(user_database, lineterminator='\r')
            data_writer.writerow(user_data)

    def Login(self):
        log = False
        while not log:
            username = input('Enter Username: ').rstrip()
            password = input('Enter Password: ')
            with open('EventIt\\Datasets\\User_database.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        if password == row[3].strip():
                            log = True
                        else:
                            print('wrong password, please try again.')
                    else:
                        print('Username Not found')
        #algo que te mande a interfaz

    def LoginAdmin(self):
        log = False
        while not log:
            username = input('Enter username: ').rstrip()
            password = input('Enter password: ')
            with open('EventIt\\Datasets\\User_database.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        if password == row[3].strip():
                            log = True
                        else:
                            print('wrong password, please try again.')
                    else:
                        print('Username Not found')
        #algo que te mande a interfaz admin


    def LoginSensor(self):
        log = False
        while not log:
            username = input('Enter Area Code: ').rstrip()
            with open('EventIt\\Datasets\\User_database.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[0].strip():
                        log = True
                    else:
                        print('Sensor Not found')
        #algo que te mande a interfaz sensor
