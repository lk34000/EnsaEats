from api.dao.order_dao import OrderDao
from api.Business_Objects.commande import Commande
from datetime import datetime
from api.dao.menu_dao import MenuDao

class OrderServices :
     
     @staticmethod
     def new_order(usernameclient : str ,idrestaurant : str):
         ''' initiates a new order from a customer and the restaurant he has chosen'''
         jour = datetime.today().replace(second = 0, microsecond = 0)
         return(Commande(username = usernameclient, id_restaurant = idrestaurant, date = str(jour)))


     @staticmethod
     def add_menu(order : Commande, menuname : str):
         ''' add a menu to an order'''
         order.contenu.append(MenuDao().find_id_by_menuname(name = menuname))
         return(order)
        
     @staticmethod
     def delete_menu(order :Commande, menuname : str):
            idmenu = MenuDao().find_id_by_menuname(menuname)
            if idmenu in order.contenu :
                i = order.contenu.index(idmenu)
                del(order.contenu[i])
            return(order)

     @staticmethod
     def consult_order(order : Commande):
        listmenus = []
        for x in order.contenu:
            listmenus += MenuDao().find_menu_by_id(x)
        return(listmenus)

     @staticmethod
     def consult_prices(order : Commande):
         price = 0
         for x in order.contenu:
             price+= MenuDao().find_price_by_id_menu(x)
         return(price)

     @staticmethod
     def register_order(order : Commande):
         ''' register an order on the physical data base'''
         OrderDao().add_order(order)
