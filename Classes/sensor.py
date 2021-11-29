from csv import writer

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
            lista_final = []
            zone_events = list()
            for line in events:
                row = line.strip().split(",")
                if self.zona == row[1]:
                    cantPersonas = len(row) - 3
                    overall_values.append(cantPersonas)
                    zone_events.append(row)
            en_orden = sorted(overall_values)
            en_orden.sort(reverse=True)
            ordenadas = en_orden[:3]
            for value in ordenadas:
                for event in zone_events:
                    if (len(event) - 3) == value :
                        texto = f"{event[2]}. {len(event) - 3} personas"
                        lista_final.append(texto)
            return lista_final

    @classmethod
    def createSensor(cls, tipo, zona):
        return cls(tipo, zona)
    

class evento:
    def __init__(self, tipo, zona, desc, gente):
        self.zona = zona
        self.tipo = tipo
        self.desc = desc
        self.gente = int(gente)
        
    def __repr__(self):
        return f"{self.tipo},{self.zona},{self.desc},{self.gente}"
        
    def __lt__(self, other):
        return self.gente < other.gente
    def __le__(self, other):
        return self.gente <= other.gente
    def __eq__(self, other):
        return self.gente == other.gente
    def __ne__(self, other):
        return self.gente != other.gente
    def __gt__(self, other):
        return self.gente > other.gente
    def __ge__(self, other):
        return self.gente >= other.gente
        
        
def listaPicos():
    with open("Datasets\Evento_pico.csv", "r", newline="") as pico:
        eventos = []
        for line in pico:
            row = line.strip().split(',')
            event = evento(row[0], row[1], row[2], row[3])
            eventos.append(event)
        orden = sorted(eventos)
        orden.sort(reverse=True)
        return orden

def checkPico(event):
    picos = listaPicos()
    if event > picos[0]:
        print(f"**** HAY UN NUEVO PICO DE {event.gente} PERSONAS ****")
        with open("Datasets\Evento_pico.csv", "a", newline="") as pico:
            pico_writer = writer(pico, lineterminator="\r")
            texto = [event.tipo,event.zona,event.desc,event.gente]
            pico_writer.writerow(texto)
            
def currentPico():
    picos = listaPicos()
    pico = picos[0]
    return pico
