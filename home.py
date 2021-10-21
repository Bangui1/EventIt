class Home: #cada funcion podria vincularse con funciones dentro de las clases de usuario (admin y ciudadano) para no darle toda la responsabilidad a Home - tamb ayuda con el tema de checkear si es o no admin
    
    #clase con interfaz una vez iniciada sesion/quiza tengamos que hacer una para admin tambien para una vez que se hace login
    #def contactoDeInteres():  def accept_request(usuario): teoricamente son lo mismo, agregar al contacto a la lista de friends
    #def reportEvent(): solicitud para agregar evento a la listaEventos
    #def request(usuario): solicitud para agregar a la lista de contactos de interes
    #def refuse_request(usario): cada vez que se rechaza un user sumar +1  
    
    #si es admin tambien puede usar
    #def blockUser(): chequear con la funcion refuse_request() si la cantidad es >= 5, si ocurre esa condicion bloquear
    #   blocked.append(usuario)
    #def unblockUser(usuario): chequear si el usuario esta bloqueado con usuario.isBlocked() , si es True desbloquearlo
    #def confirmEvent(): agregar un valor al evento donde confirma para agrandar la cantidad de participanted de dicho evento y hacerlo "mas rojo"
    #posible agregar un addAdmin() y kickAdmin()
#   def isBlocked(self,usuario):# valor si esta bloqueado o no
#       for i in self.blocked:
#           if usuario == i:
#               return True
#       return False
    pass
