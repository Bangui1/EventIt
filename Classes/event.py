from csv import writer

def checkCantidad():
    try:
        cant = input("¿Cuántas conocidos forman parte del evento?: ")
        if int(cant) <= 0:
            raise ValueError
        else:
            return cant
    except:
        print("Error. Utilizar números positivos")
        checkCantidad()
            
def addPeople():
    with open('Datasets\\User_database.csv', 'a', newline='') as user_database:
        cant = checkCantidad()
        people = []
        i = 0
        while i in range(cant):
            user = input("Ingresar usuario que forme parte del evento: ")
            try:
                found = False
                for line in user_database:
                    row = line.strip().split(',')
                    if user == row[2]:
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
            seleccion = input("\nNúmero del tipo de evento que quiere elegir: ")
            sel = int(seleccion)
            stop = 0
            for line in tipos:
                row = line.strip().split(",")
                if stop == sel:
                    return row
                stop += 1
        except:
            print("debe ingresar un número que este dentro del rango")
            seleccionarTiposEvent()

def getZone():
    with open('Datasets\\CurrentUser.csv', 'r', newline='') as user:
        for line in user:
            cuil = line
        with open('Datasets\\dataset_Anses.csv', 'r', newline='') as user_data:
            for line in user_data:
                row = line.strip().split(",")
                if row[0] == cuil:
                    return row[2]
                
def requestEvent():
    tipo = seleccionarTiposEvent()
    zona = getZone()
    gente = addPeople()
    with open('Datasets\\Event_requests.csv', 'a', newline='') as reqs:
        event_data = [tipo, zona, gente]
        data_writer = writer(reqs, lineterminator='\r')
        data_writer.writerow(event_data)
    
        
class sensor:
    # def __init__(self):
    #     self.listaSensores = [] #esto podria ir en el login 
   
    def getInfo(self,event): 
        for i in self.listaSensores:
            if i == event:
                return event.getType()
