from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.notificaciones = [] #para los admins quizas se puede usar la primer linea del csv como lista de notifs, creando tambien una classe de notifs
        

class Ciudadano(Usuario):
    #se registra en el sistema mediante Register() en Home
    def __init__(self, username, password, CUIL, telefono):
        Usuario.__init__(self, username, password)
        self.cuil = CUIL
        self.telefono = telefono
        self.friends = []
        self.NoOfTimesRejected = 0
        self.pendingRequests = []
        self.BlockedState = False
    
    def __repr__(self):
        return f"{self.username} - Tel: {self.telefono} - CUIL: {self.cuil}"
        
