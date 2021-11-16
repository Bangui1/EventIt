class event:
    def __init__(self, tipo, zone, interesados):
        self.tipo = tipo
        self.zone = zone #estilo (a,b) o como se maneje el mapa
        self.interesados = []
    
    
    def getType(self):
        return self.type





    @classmethod
    def create_event(cls, tipo, zone):
        return cls(tipo, zone)
        
#idea de solicitud de event (usuario)
# def solicitar_evento(self):
#     with open('event_types.csv')
#     seleccionar_tipo = input('ingrese el numero')
#     return event.create_event(seleccionar_tipo, self.zone)



        
class sensor:
    # def __init__(self):
    #     self.listaSensores = [] #esto podria ir en el login 
   
    def getInfo(self,event): 
        for i in self.listaSensores:
            if i == event:
                return event.getType()
