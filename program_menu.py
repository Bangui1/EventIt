from menu_admin import menu_admin
from menu_users import menu_user
from login import menuLogin
class Menu:
    def mainMenu(self):
        print('\n\n\n\nWelcome to the program')
        running = True
        while running:
            try:
                print('\n\nPlease select a menu: \n1.- Register \t2.- Login as user \t3.- Login as Admin \t4.- Enter as Sensor \t5.- Exit Program')
                menu_input = input('Enter menu number: ')
                if menu_input == '1':
                    menuLogin.Register(self)
                elif menu_input == '2':
                    menuLogin.user_mainMenu(self)
                elif menu_input == '3':
                    menu_admin.Admin_mainMenu(self)
                elif menu_input == '4':
                    menuLogin.LoginSensor(self)
                elif menu_input == '5':
                    print('Logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n\n')
    

