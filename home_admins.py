from csv import writer


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
                username = input('Enter your username: ')
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


    def acceptEventRequest(self):
        with open('Datasets\\Events_requests.csv', 'r', newline='') as rqts:
            i = 0
            for line in rqts:
                row = line.strip().split(",")
                print("Eventos a ser aceptados:\n")
                print(f"{i}.\t{row}")
            try:
                acceptee = input("Número del evento que quiere aceptar: ")
                acc = int(acceptee)
                num = 0
                for line in rqts:
                    row2 = line.strip().split()
                    if num == acc:
                        writer_rqts = writer(rqts, lineterminator="\r")
                        writer_rqts.writerow(line)
                    num += 1
                    with open('Datasets\\Events_database.csv', 'a', newline='') as events:
                        writer_eventos = writer(events, lineterminator="\r")
                        writer_eventos.writerow(row2)
            except:
                print("número fuera de rango") 
                    
    def denyEventRequest(self):
        with open('Datasets\\Events_requests.csv', 'a', newline='') as rqts:
            i = 0
            for line in rqts:
                row = line.strip().split(",")
                print("Eventos a ser rechazados:\n")
                print(f"{i}.\t{row}")
            try:
                denied = input("Número del evento que quiere rechazar: ")
                den = int(denied)
                num = 0
                for line in rqts:
                    row2 = line.strip().split()
                    if num == den:
                        writer_rqts = writer(rqts, lineterminator="\r")
                        writer_rqts.writerow(line)
            except:
                print("número fuera de rango")
        
intAdmin = InterfazAdmin()
