from Classes.users import Admin
from csv import writer

class Home: #cada funcion podria vincularse con funciones dentro de las clases de usuario (admin y ciudadano) para no darle toda la responsabilidad a Home - tamb ayuda con el tema de checkear si es o no admin
    
    #clase con interfaz una vez iniciada sesion/quiza tengamos que hacer una para admin tambien para una vez que se hace login
    #def contactoDeInteres():  def accept_request(usuario): teoricamente son lo mismo, agregar al contacto a la lista de friends
    #def reportEvent(): solicitud para agregar evento a la listaEventos
    #def request(usuario): solicitud para agregar a la lista de contactos de interes
    #def refuse_request(usario): cada vez que se rechaza un user sumar +1  
    
    #si es admin tambien puede usar
    #def blockUser(): chequear con la funcion refuse_request() si la cantidad es >= 5, si ocurre esa condicion bloquear
    #   blocked.append(usuario)
    #def unblockUser(usuario): chequear si el usuario esta bloqueado con usuario.isBlocked() , si es True desbloquearlo
    #def confirmEvent(): agregar un valor al evento donde confirma para agrandar la cantidad de participanted de dicho evento y hacerlo "mas rojo"
    #posible agregar un addAdmin() y kickAdmin()
#   def isBlocked(self,usuario):# valor si esta bloqueado o no
#       for i in self.blocked:
#           if usuario == i:
#               return True
#       return False
    pass

class InterfazUser:
    pass

class InterfazAdmin:
    def checkIfBlocked(username):
        with open('Datasets\\User_database.csv', 'a', newline='') as user_database:
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        return row[5].blockedState
                if found:
                    pass
                else:
                    raise ValueError
            except:
                print("User not found.")

    
    def blockUser(self):
        username = input("Ingresar nombre del usuario al cual quiere bloquear: ")
        with open('Datasets\\User_database.csv', 'a', newline='') as user_database:
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        found = True
                        if InterfazAdmin.checkIfBlocked(username) == False:
                            row[5].blockedState = True
                        else:
                            print("User already blocked!")
                if found:
                    pass
                else:
                    raise ValueError
            except:
                print('Username Not found')

    def unblockUser(self):
        username = input("Ingresar nombre del usuario al cual quiere bloquear: ")
        with open('Datasets\\User_database.csv', 'a', newline='') as user_database:
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
                        found = True
                        if InterfazAdmin.checkIfBlocked(username):
                            row[5].blockedState = False
                        else:
                            print("User is not blocked!")
                if found:
                    pass
                else:
                    raise ValueError
            except:
                print("Username Not Found")

    def CheckAdmin(self):
        with open('Datasets\\Admin_dataset.csv', 'r') as user_database:
            check = False
            while check == False:
                username = input('Enter your username: ')
                for line in user_database:
                    row = line.strip().split(',')
                    if username == row[2].strip():
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
        username = InterfazAdmin.CheckAdmin()
        password = InterfazAdmin.CheckPassword()
        with open('Datasets\\Admin_dataset.csv', 'a', newline='') as adm_database:
            admin = Admin(username, password)
            adm_data = [admin.username, admin.password]
            data_writer = writer(adm_database, lineterminator='\r')
            data_writer.writerow(adm_data)

    def banAdmin(self):
        user = input("Ingresar usuario del admin que quiere kickear: ")
        with open('Datasets\\Admin_dataset.csv', 'a', newline='') as adm_database:
            data_writer = writer(adm_database, lineterminator='\r')
            try:
                found = False
                for line in adm_database:
                    row = line.strip().split(',')
                    if user == row[0].strip():
                        found = True
                        data_writer.writerow(row) #se supone que lo deberia borrar
                if found:
                    pass
                else:
                    raise ValueError
            except:
                print("Admin not found")
                
    def acceptEventRequest(self):
        with open('Datasets\\Events_requests.csv', 'a', newline='') as rqts:
            i = 0
            for line in rqts:
                row = line.strip().split(",")
                print("Eventos a ser aceptados:\n")
                print("{i}.\t{row}")
            try:
                with open('Datasets\\Events_database.csv', 'a', newline='') as events:
                    acceptee = input("Número de evento que quiere aceptar: ")
                    acc = int(acceptee)
                    num = 0
                    for line in events:
                        row = line.strip().split(",")
                        if acc == num:
                            writer_events = writer(events, lineterminator="\r")
                            writer_events.writerow()
                            otro = 0
                            for line in rqts:
                                if otro == acc:
                                    writer_rqts = writer(rqts, lineterminator='\r')
                                    writer_rqts.writerow("")  # no se si lo borra  
                                otro += 1    
                        num += 1
            except:
                print("número fuera de rango")
                        
        






#interfaz sensor puede ser un mapa
