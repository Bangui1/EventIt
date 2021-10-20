from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, CUIL, password, telefono):
        self.cuil = CUIL
        self.password = password
        self.telefono = telefono

class Admin(Usuario): 
    #no se registra en el sistema, se crea con login y contraseña predeterminada
    #metodo para habilitar eventos
    pass

class Ciudadano(Usuario):
    #se registra en el sistema
    friends = [] #lista de contactos de interes
    blocked = [] #usuarios bloqueados
  
