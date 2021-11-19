from csv import writer

def checkCantidad():
    try:
        cant = input("¿Cuántas conocidos forman parte del evento?: ")
        if cant > 0:
            raise ValueError
        else:
            return cant
    except:
        print("Error. Utilizar números positivos")
        checkCantidad()
            
def addPeople():
    with open('Datasets\\User_database.csv', 'a', newline='') as user_database:
        cant = int(checkCantidad())
        people = []
        i = 0
        while i in range(cant):
            user = int(input("Ingresar CUIL o telefono de usuario que forme parte del evento: "))
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if user == row[0] or row[1]:
                        people.append(user)
                        found = True
                        i += 1
                if found:
                    pass
                else:
                    raise ValueError
            except:
                print("User not found. Try again")
                addPeople()
        return people
       
def seleccionarTiposEvent():
    with open('Datasets\\Event_types.csv', 'r', newline='') as tipos:
        i = 0
        for line in tipos:
            row = line.strip().split(",")
            print(f"{i}. {row}")
            i += 1
    try:
        with open('Datasets\\Event_types.csv', 'r', newline = '') as tipos:
            seleccion = input("\nNúmero del tipo de evento que quiere elegir: ")
            sel = int(seleccion)
            stop = 0
            for line in tipos:
                row2 = line.strip().split(",")
                if stop == sel:
                    return row2[0]
                stop += 1
    except:
        print("debe ingresar un número que este dentro del rango")
        seleccionarTiposEvent()

def getZone():
    with open('Datasets\\CurrentUser.csv', 'r', newline='') as user:
        for line in user:
            row = line.strip().split(",")
            cuil = row[0]
        with open('Datasets\\Anses_dataset.csv', 'r', newline='') as user_data:
            for line in user_data:
                row = line.strip().split(",")
                if row[0] == cuil:
                    return row[2]
                
def requestEvent():
    tipo = seleccionarTiposEvent()
    zona = getZone()
    gente = addPeople()
    info = input("Describir el evento: ")
    with open('Datasets\\Event_requests.csv', 'a', newline='') as reqs:
        event_data = [tipo, zona, info, gente]
        data_writer = writer(reqs, lineterminator='\r')
        data_writer.writerow(event_data)
    
        

