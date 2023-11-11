from api.Business_Objects.menu import Menu
from api.dao.menu_dao import MenuDao
''' Here we will propose the list of menus from the restaurant chosen by the user according to the user's choices,
he can add or not the menu he wants to his order.
The menus are taken from the DAO with the id of the restaurant chosen before with restaurant_services.
As long as the user has not finished his order, he can add menus.
The final order is processed and sent to the physical database in order to obtain an order history.'''





class MenuServices :
    ''' Send back menus proposed by the restaurant when the customer has chosen his restaurant'''
    @staticmethod
    def get_menus(idrestaurant: str):
        return(MenuDao().find_menu_by_restaurant(idrestaurant))

    @staticmethod
    def add_menu_dao(menu : Menu):
        return(MenuDao().add_menu(menu))

    @staticmethod
    def del_menu_dao(menu : Menu):
        return(MenuDao().del_menu(menu))
    

    
    
    


