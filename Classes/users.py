from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, CUIL, password, telefono,blocked,friends):
        self.cuil = CUIL
        self.password = password
        self.telefono = telefono
        self.blocked = []
        self.friends = []

class Admin(Usuario): 
    #no se registra en el sistema, se crea con login y contraseña predeterminada
    #metodo para habilitar eventos
    #bloquear y desbloquear ciudadanos
    pass

class Ciudadano(Usuario):
    #se registra en el sistema
    # o se logea en el sistema
    pass
  
