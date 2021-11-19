class Sensor:
    def __init__(self, tipoDeEvento, nombreZona):
        self.tipo = tipoDeEvento
        self.zona = nombreZona

    def getInfo(self):
        print("Current events in this zone: \n")
        with open('Datasets\\Events_database.csv', 'r', newline='') as events:
            i = 0
            for line in events:
                row = line.strip().split(",")
                if row[1] == self.zona and row[0] == self.tipo:
                    print(f"{i}.\tTipo: {row[0]}. Desc: {row[2]}. Cant de concurrentes: {len(row) - 3}")
                    i += 1
                    
    def top3Zona(self):
        with open('Datasets\\Events_database.csv', 'r', newline='') as events:
            overall_values = []
            for line in events:
                row = line.strip().split(",")
                if self.zona == row[1]:
                    cantPersonas = len(row) - 3
                    overall_values.append(cantPersonas)
            en_orden = sorted(overall_values)
            en_orden.sort(reverse=True)
            return en_orden[:4]
        
    @property
    def listaParaPicos(self): #NO SE TIENE EN CUENTA LA ZONA NI TIPO - SON PICOS OVERALL
        with open('Datasets\\Event_database.csv', 'r', newline='') as events:
            overall_values = []
            for line in events:
                row = line.strip().split(",")
                cantPersonas = len(row) - 3
                overall_values.append(cantPersonas)
            ordenada = sorted(overall_values)
            ordenada.sort(reverse=True)
            return ordenada
        
    def checkPico(self, value):
        listaParaCheck = self.listaParaPicos
        if value > listaParaCheck[0]:
            print(f"HAY UN NUEVO PICO DE {value} PERSONAS")

    @classmethod
    def createSensor(cls, tipo, zona):
        return cls(tipo, zona)