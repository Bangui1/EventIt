from abc import ABC, abstractmethod, classmethod
class Usuario(ABC):
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.notificaciones = []
        
class Sensor:
    def __init__(self, number, zona):
        self.num = number
        self.zona = zona
        

class Admin(Usuario): 
    #no se registra en el sistema, se crea con login y contraseña predeterminada
    notifsEventos = []
    
    def banUser(self, usuario):
        #buscar en ambos datasets de usuarios y bloqueados - checkear BLockedState - de ser posible cambiarlo a True y agregar a dataset de bloqueados
        pass
    
    def unbanUser(self, usuario):
        pass
    
    @classmethod
    def confirmEvent(cls, event):
        #chequear en lista de notifs x los eventos y aceptar para que aparezca para los sensores - quizas se puede armar la lista en orden de mas solicitudes
        pass
    
    @classmethod
    def denyEvent(cls, event):
        pass

class Ciudadano(Usuario):
    #se registra en el sistema mediante Register() en Home
    def __init__(self, username, password, CUIL, telefono):
        Usuario.__init__(username, password)
        self.cuil = CUIL
        self.telefono = telefono
        self.friends = []
        self.NoOfTimesRejected = 0
        self.pendingRequests = []
        self.BlockedState = False
        
    def requestFriend(self, CUIL):
        #enviar notificacion y agregar a pendingRequests del otro usuario con opcion de aceptar o denegar
        pass
    
    def addFriend(self, username):
        #se elimina la notif y se agrega el usuario a lista friends
        pass
    
    def refuseFriend(self, username):
        # +1 a NoOfTimesRejected del usuario -> un check si es >5 - si es cambiar BlockedState a True y agregar a dataset de bloqueados
        pass
    
    def report_event(self): #completar los parentesis con tipo de evento para crearlo - despues enviar notificacion a administradores para aceptar/denegar
        pass  
