from Classes.event import requestEvent, checkCantidad, addPeople, seleccionarTiposEvent, getZone

class InterfazUser:
    @property
    def currentUser(self):
        with open('Datasets\\CurrentUser.csv', 'r', newline='') as user:
            for line in user:
                row = line.strip().split(",")
                usuario = row[2]
            return usuario
    
    def contactoDeInteres(self):
        with open('Datasets\\User_database.csv', 'r', newline='') as user_database:
            other_user = input("Escribir el CUIL o celular al que quiere agregar como amigo: ")
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(",")
                    if row[0] == other_user or row[1] == other_user:
                        found = True
                        #USAR WITH OPEN(EL ARCHIVO DEL OTHER_USER) -> Notificaciones.append(self.currentUser) // (notificaciones vendria a ser la linea donde estan las notifs)
                if found:
                    pass
                else:
                    raise ValueError
            except ValueError:
                print("Usuario no encontrado: ")
    
    def check_requests(self):
        with open('EL NOMBRE DEL ARCHIVO QUE TENGA LAS NOTIFICACIONES DEL CURRENT USER', 'r', newline='') as user_data:  # CAMBIAR PATH
            i = 0
            for line in user_data:
                row = line.strip().split(",")
                if i == EL_NUMERO_DONDE_ESTEN_LAS_NOTIFS:
                    count = 0
                    while count < len(row):
                        print(row[count])
                        try:
                            action = input("Desea aceptar la solicitud (Y/N): ")
                            if action.lower() == "n":
                                #DELETE Y +1 AL BLOCK COUNT DEL USUARIO QUE LA MANDO
                                count += 1
                            elif action.lower() == "y":
                                #DELETE Y AGREGAR A LA LISTA DE AMIGOS EN AMBOS ARCHIVOS DE USUARIO
                                count += 1
                            else:
                                raise ValueError                                
                        except ValueError:
                            print("wrong input, try again")
                i += 1
    
    def reportEvent(self):
        return requestEvent()
    
intUser = InterfazUser()