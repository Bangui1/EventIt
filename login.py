# import pandas
# from Classes.datasets import datasetANSES, datasetUSUARIOS, datasetBLOQUEADOS
# from Classes.users import Usuario, Admin, Ciudadano, Sensor
# class Login:
#     def register(celular, CUIL, username, password): #usar manejo de archivos para poder crear usuarios y escribirlos en un .txt o .csv(usando pandas)
#         for n in datasetANSES.ciudadanos:
#             if n.cuil == CUIL:
#                 user = Ciudadano(username, password, CUIL, celular)
#                 datasetUSUARIOS.ciudadanos_user.append(user)
#             else:
#                 return "No se encontró el cuil en la base de datos"
#     def login(username, password): #leer y buscar en el archivo donde se guardan los usuarios
#     for i in datasetUSUARIOS.ciudadanos_user: #lstUsers va a ser un csv que tenga en cada valor un usuario y su contraseña
#         if username == i.username and password == i.password
#             #login como usuario comun
#         else:
#             for i in datasetUSUARIOS.administradores:
#                 if username == i.username and password == i.password
#                     #login como admin
#             else:
#                 return "Usuario o contraseña incorrectos. Reescribir y reintentar"
#     def entrar_como_sensor(numero): #crear un acceso especial sin login para los sensores
#         for s in datasetUSUARIOS.sensores:
#             if s.num == numero:
#                 #login como sensor - otra interfaz que no es como la de usuario - solo tiene habilitado la funcion de getInfo()
#             else:
#                 return "ese sensor no existe"

#login usando archivos .csv 

class Start:
    def Login(self):
        log = False
        while not log:
            username = input('Enter Username: ').rstrip()
            password = input('Enter Password: ')
            with open('Usuarios_registrados.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if username == row[0].strip():
                        if password == row[1].strip():
                            log = True
                        else:
                            print('wrong password, please try again.')
                    else:
                        print ('Username Not found')


    def Register(self):
        register = False
        while not register:
            cuil = input('Please enter your CUIL: ')
            with open('dataset_Anses.csv', 'r') as database:
                for line in database:
                    row = line.strip().split(',')
                    if cuil == row[0]:
                        register = True
