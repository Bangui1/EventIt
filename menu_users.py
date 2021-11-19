from home_usuarios import intUser

class UserMenu:

    def User_mainMenu(self):
        print(f'\n\n\n\nWelcome to EventIt, {intUser.currentUser}')
        running = True
        while running:
            try:
                print('\n\nPlease select a menu: \n1.- Event menu \t2.- Contacts \t3.- Exit Program')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    UserMenu.User_eventMenu(self)
                elif menu_input == '2':
                    UserMenu.User_contactMenu(self)
                elif menu_input == '3':
                    print('logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.')


    def User_eventMenu(self):
        print(f'\n\n\n\nEvent menu.')
        running = True
        while running:
            try:
                print('\n\nPlease select an action: \n1.- Report Event \t2.- Return to main menu')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    intUser.reportEvent()
                elif menu_input == '2':
                    print('logging off. Exiting program.')
                    running = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.')

    def User_contactMenu(self):
        print(f'\n\n\n\nContact menu.')
        running = True
        while running:
            try:
                print('\n\nPlease select an action: \n1.- Enviar solicitud \t2.- Ver solicitudes \t3.- Return to main menu')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    intUser.contactoDeInteres()
                elif menu_input == '2':
                    intUser.check_requests()
                elif menu_input == '3':
                    running = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.')






menu_user = UserMenu()
