class event:
    def __init__(self, tipo, coords):
        self.tipo = tipo
        self.coords = coords #estilo (a,b) o como se maneje el mapa
    
    def getType(self):
        return self.type

class sensor:
    # def __init__(self):
    #     self.listaSensores = [] #esto podria ir en el login 
   
    def getInfo(self,event): 
        for i in self.listaSensores:
            if i == event:
                return event.getType()
