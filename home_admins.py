from csv import writer
from Classes.sensor import checkPico, evento

class InterfazAdmin:
    def checkIfBlocked(self, username):
        with open('Datasets\\User_database.csv', 'r', newline='') as user_database:
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        found = True
                        return row[4] == 'Blocked'
                if found:
                    pass
                else:
                    raise ValueError
            except ValueError:
                print("User not found.")

    
    def blockUser(self):
        try:
            username = input("Ingresar nombre del usuario al cual quiere bloquear: ")
            with open('Datasets\\User_database.csv', 'r', newline='') as user_database:
                found = False
                user_data = list()
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        found = True
                        if not InterfazAdmin.checkIfBlocked(self, username):
                            row[4] = 'Blocked'
                            with open(f'Users\\{row[0]}.csv', 'r', newline='') as user_database:
                                user_data2 = list()
                                for line in user_database:
                                    row2 = line.strip().split(',')
                                    if row[0] == row2[0].strip():
                                        row2[4] = 'Blocked'
                                    user_data2.append(row2)

                            with open(f'Users\\{row[0]}.csv', 'w', newline = '') as user_database:
                                data_writer = writer(user_database, lineterminator = '\r')
                                for data in user_data2:
                                    data_writer.writerow(data)
                            print('User successfuly Blocked.')
                        else:
                            print("User already blocked!")
                    user_data.append(row)
            if found:
                with open('Datasets\\User_database.csv', 'w', newline = '') as user_database:
                    data_writer = writer(user_database, lineterminator = '\r')
                    for data in user_data:
                        data_writer.writerow(data)
            else:
                raise ValueError
        except ValueError:
            print('Username Not found')


    def auto_BlockUser(self, cuil):
        with open(f'Users\\{cuil}.csv', 'r', newline='') as user_database:
                user_data = list()
                for line in user_database:
                    row = line.strip().split(',')
                    if cuil == row[0].strip():
                        row[4] = 'Blocked'
                    user_data.append(row)

        with open(f'Users\\{cuil}.csv', 'w', newline = '') as user_database:
            data_writer = writer(user_database, lineterminator = '\r')
            for data in user_data:
                data_writer.writerow(data)


            with open('Datasets\\User_database.csv', 'r', newline='') as user_database:
                user_data = list()
                for line in user_database:
                    row = line.strip().split(',')
                    if cuil == row[0].strip():
                        row[4] = 'Blocked'
                    user_data.append(row)
            with open('Datasets\\User_database.csv', 'w', newline = '') as user_database:
                data_writer = writer(user_database, lineterminator = '\r')
                for data in user_data:
                    data_writer.writerow(data)

    def unblockUser(self):
        try:
            username = input("Ingresar nombre del usuario al cual quiere desbloquear: ")
            found = False
            user_data = list()
            with open('Datasets\\User_database.csv', 'r', newline='') as user_database:
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        found = True
                        if InterfazAdmin.checkIfBlocked(self, username):
                            row[4] = 'Unblocked'
                            row[5] = '0'
                            with open(f'Users\\{row[0]}.csv', 'r', newline='') as user_database:
                                user_data2 = list()
                                for line in user_database:
                                    row2 = line.strip().split(',')
                                    if row[0] == row2[0].strip():
                                        row2[4] = 'Unblocked'
                                        row2[5] = '0'
                                    user_data2.append(row2)

                            with open(f'Users\\{row[0]}.csv', 'w', newline = '') as user_database:
                                data_writer = writer(user_database, lineterminator = '\r')
                                for data in user_data2:
                                    data_writer.writerow(data)

                            print('\nUser successfuly Unblocked.')
                        else:
                            print("User is not blocked!")
                    user_data.append(row)
                    
            if found:
                with open('Datasets\\User_database.csv', 'w', newline= '') as user_database:
                    data_writer = writer(user_database, lineterminator = '\r')
                    for data in user_data:
                        data_writer.writerow(data)
            else:
                raise ValueError
        except ValueError:
            print("Username Not Found")




    def CheckAdmin(self):
        with open('Datasets\\Admin_dataset.csv', 'r') as user_database:
            check = False
            while check == False:
                username = input('Enter new username: ')
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[0].strip():
                        print("Username already exist, try another one")
                        InterfazAdmin.checkAdmin()
                    else:
                        check = True
                        return username
    
    def CheckPassword(self):
        check = False
        while check == False:
            password = input('Enter your password: ')
            confirm_password = input('Please re-enter your password:')
            if password != confirm_password:
                print('Passwords do not match, please try again.')
                InterfazAdmin.checkPassword(self)
            else:
                check = True
                return password

    def addAdmin(self):
        username = InterfazAdmin.CheckAdmin(self)
        password = InterfazAdmin.CheckPassword(self)
        with open('Datasets\\Admin_dataset.csv', 'a', newline='') as adm_database:
            adm_data = [username, password]
            data_writer = writer(adm_database, lineterminator='\r')
            data_writer.writerow(adm_data)

    def banAdmin(self):
        user = input("Ingresar usuario del admin que quiere kickear: ")
        with open('Datasets\\Admin_dataset.csv', 'r', newline='') as adm_database:
            try:
                found = False
                file_list = list()
                for line in adm_database:
                    row = line.strip().split(',')
                    if row[0] == user:
                        del(row)
                        found = True
                    else:
                        file_list.append(row)

                with open('Datasets\\Admin_dataset.csv', 'w', newline= '') as adm_database:
                    data_writer = writer(adm_database, lineterminator = '\r')
                    for admin_data in file_list:
                        data_writer.writerow(admin_data)
                if found:
                    pass
                else:
                    raise ValueError
            except ValueError:
                print("Admin not found")


    def printRequests(self):
        with open('Datasets\\Events_requests.csv', 'r', newline='') as rqts:
            try:
                i = 0
                print("\nEventos a ser aceptados:\n")
                for line in rqts:
                    row = line.strip().split(",")
                    print(f"{i}.\t{row}\n")
                    i += 1
                acceptee = input("Número del evento que quiere aceptar: ")
                return int(acceptee)
            except:
                print("numero fuera de rango. Reintentar")
                self.printRequests()

    def acceptEventRequest(self):
        numero = self.printRequests()
        try:
            acc = int(numero)
            with open('Datasets\\Events_requests.csv', 'r', newline='') as rqts:
                num = 0
                request_data = list()
                for line in rqts:
                    row = line.strip().split(',')
                    if num == acc:
                        event = evento(row[0], row[1], row[2], (len(row) - 3))
                        checkPico(event)
                        with open('Datasets\\Events_database.csv', 'a', newline='') as events:
                            writer_eventos = writer(events, lineterminator="\r")
                            writer_eventos.writerow(row)
                        num += 1
                    else:
                        num += 1
                        request_data.append(row)
            with open('Datasets\\Events_requests.csv', 'w', newline = '') as requests:
                data_writer = writer(requests, lineterminator = '\r')
                for data in request_data:
                    data_writer.writerow(data)

        except ValueError:
            print("número fuera de rango") 
                    
    def denyEventRequest(self):
        numero = self.printRequests()
        try:
            acc = int(numero)
            with open('Datasets\\Events_requests.csv', 'r', newline='') as rqts:
                num = 0
                request_data = list()
                for line in rqts:
                    row = line.strip().split(',')
                    if num != acc:
                        request_data.append(row)
                    num += 1
            
            with open('Datasets\\Events_requests.csv', 'w', newline = '') as requests:
                data_writer = writer(requests, lineterminator = '\r')
                for data in request_data:
                    data_writer.writerow(data)

        except ValueError:
            print("número fuera de rango") 
        
intAdmin = InterfazAdmin()
