
from csv import writer

class Start:
    def Login(self):
        log = False
        while not log:
            username = input('Enter Username: ').rstrip()
            password = input('Enter Password: ')
            with open('Datasets\\User_database.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        if password == row[3].strip():
                            log = True
                        else:
                            print('wrong password, please try again.')
                    else:
                        print ('Username Not found')


    def Register(self):
        register = False
        while not register:
            cuil = input('Please enter your CUIL: ')
            phone_number = input('Please enter your phone number: ')
            username = input('Enter your username: ')
            
            check_password = False
            while not check_password:
                password = input('Enter your password: ')
                confirm_password = input('Please re-enter your password:')
                if password == confirm_password:
                    check_password = True
                else:
                    print('Passwords do not match, please try again.')


            with open('Datasets\\dataset_Anses.csv', 'r', newline = '') as database:
                for line in database:
                    row = line.strip().split(',')
                    if cuil == row[0]:
                        with open('Datasets\\User_database.csv', 'a') as user_database:
                            user_data = [cuil, phone_number, username, password]
                            data_writer = writer(user_database, lineterminator='\r')
                            data_writer.writerow(user_data)
                            register = True
                            break
            if register:
                print('successful registration')
            else:
                print('CUIL not found in dataset, please try again')


    def LoginAdmin(self):
        log = False
        while not log:
            username = input('Enter Username: ').rstrip()
            password = input('Enter Password: ')
            with open('Datasets\\Admin_dataset.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[0].strip():
                        if password == row[1].strip():
                            log = True
                        else:
                            print('wrong password, please try again.')
                    else:
                        print('Username Not found')


    def LoginSensor(self):
        log = False
        while not log:
            username = input('Enter Area Code: ').rstrip()
            with open('Datasets\\Sensor_dataset.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[0].strip():
                        log = True
                    else:
                        print('Sensor Not found')
