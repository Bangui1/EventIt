from home_usuarios import intUser

class UserMenu:

    def User_mainMenu(self):
        print(f'\n\n\n\nWelcome to EventIt, {intUser.currentUser}')
        running = True
        while running:
            try:
                print('\n\nPlease select a menu: \n1.- Event menu \t2.- Contacts \t3.- Feed \t4.- Exit Program')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    pass #def User_EventMenu
                if menu_input == '2':
                    pass
            except ValueError:
                pass

menu_user = UserMenu()
