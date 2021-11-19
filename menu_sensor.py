from Classes.sensor import Sensor
from Classes.map import enter_map


class SensorMenu:
    
    def sensor_mainMenu(self, sensor):
        print('\n\n\n\nWelcome to the program')
        running = True
        while running:
            try:
                print('\n\nPlease select a menu: \n1.- Mostrar top 3 zona \t2.- Mostrar info \t3.- Abrir Mapa\t4. - Exit Program')
                menu_input = input('Enter menu number: ')
                if menu_input == '1':
                    print(sensor.top3Zona())
                elif menu_input == '2':
                    sensor.getInfo()
                elif menu_input == '3':
                    enter_map()
                elif menu_input == "4":
                    print('Logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n\n')

senMenu = SensorMenu()