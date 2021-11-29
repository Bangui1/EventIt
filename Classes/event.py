from csv import writer

def checkCantidad():
    try:
        cant = input("¿Cuántas conocidos forman parte del evento?: ")
        if int(cant) < 0:
            raise ValueError
        else:
            return int(cant)
    except ValueError:
        print("Error. Utilizar números positivos")
        checkCantidad()
            
def addPeople():
    cant = int(checkCantidad())
    people = []
    try:
        i = 0
        while i in range(cant):
            with open('Datasets\\User_database.csv', 'r', newline='') as user_database:
                user = input("Ingresar CUIL o telefono de usuario que forme parte del evento: ")
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if user == row[0] or user == row[1]:
                        people.append(int(user))
                        found = True
                if found:
                    i += 1
                else:
                    raise ValueError
    except ValueError:
        print("User not found. Try again")
        addPeople()
    people_text = list()
    count = 0
    while count < len(people):
        people_text.append(str(people[count]))
        count += 1
    return people_text
       
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
        i = 0
        for line in user:
            if i == 0:
                row = line.strip().split(",")
                cuil = row[0]
            i += 1
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

    with open('Datasets\\Events_requests.csv', 'a', newline='') as reqs:
        event_data = [tipo, zona, info]
        for people in gente:
            event_data.append(people.strip())
        data_writer = writer(reqs, lineterminator='\r')
        data_writer.writerow(event_data)
    
        

