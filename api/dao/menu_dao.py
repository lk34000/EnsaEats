from typing import List, Optional
from api.Business_Objects.plat import Plat
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.Business_Objects.menu import Menu
from api.dao.dish_dao import DishDao




class MenuDao(metaclass=Singleton):
    def find_all_menus(self, limit=0, offest: int=0) -> List[Menu]:
        """
        Get all menus in the db without any filters
        :param limit: how many menus are requested
        :type limit: int
        :param offest: the offset of the request
        :type offest: int
        """
        request= "SELECT * FROM ensaeats.menu"
        if limit :
            request+=f"LIMIT {limit}"
        if offest :
            request+=f"OFFSET {offest}"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                )
                res = cursor.fetchall()
        return (res)

    def find_menu_by_id(self, id_menu:int)-> Optional[Menu]:
        """
        Get a menu with a specific id. Return None if there is no menu

        :param id_menu: the menu id
        :type id_menu: int
        :return: the menu
        :rtype: Optional[menu]
        """
        with DBConnection().connection as connection:
            ##search of key points
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * from ensaeats.menu "\
                    "WHERE id_menu=%(id)s"
                , {"id" : id_menu})
                res = cursor.fetchone()

                ##search of dishes which composed a menu
                cursor.execute(
                    "SELECT * from "
                    "ensaeats.plat as p, ensaeats.menu_plat as mp "
                    "WHERE mp.id_menu=%(id)s"
                    " and p.id_plat = mp.id_plat"
                , {"id" : id_menu})
                res2 = cursor.fetchall()
                list_dish = []
                for i in range(len(res2)) : 
                    ligne = res2[i]
                    p=Plat(nom = ligne['nom_plat'], id_restaurant = res['nomresto'])
                    list_dish.append(p)

        searched_menu = None

        if res :
            searched_menu = Menu(
              nom = res['nom_menu']
             , idrestaurant = res['nomresto']
             , prix = res['prix']
             ,listplat = list_dish
            
            )

        return (searched_menu)


    def find_id_by_menuname(self,name : str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_menu FROM ensaeats.menu "
                    " WHERE nom_menu = %(name)s"
                ,{'name' : name})
                res = cursor.fetchone()
        if res:
            return (res["id_menu"])


    def find_menu_by_restaurant(self, restaurant:str):
        """
        Get a menu from a specific restaurant. Return None if there is no menu

        :param restaurant : the restaurant name
        :type restaurant: str
        :return: the menus from the restaurant
        :rtype: List[menu]
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM ensaeats.menu "\
                    "WHERE nomresto=%(nom)s"
                    , {"nom" : restaurant} )
                res=cursor.fetchall()

        liste_menu =[]
        for i in range(len(res)) :
            objet_menu = Menu(nom =res[i]['nom_menu'],
                            idrestaurant =restaurant,
                            prix = res[i]['prix'],
                            listplat =DishDao().find_dish_by_menu(res[i]['id_menu']))
            liste_menu.append(objet_menu)


        return (liste_menu)

    def find_id_by_menuname(self,name : str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_menu FROM ensaeats.menu "
                    " WHERE nom_menu = %(name)s"
                ,{'name' : name})
                res = cursor.fetchone()
        if res:
            return (res["id_menu"])

    def find_price_by_id_menu(self,id_menu):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT m.prix "
                    "FROM ensaeats.menu as m "
                    "where m.id_menu = %(idm)s " ,{'idm' : id_menu}
                )
                res = cursor.fetchone()
        return(res['prix'])

    def find_id_menu_by_restaurant(self, restaurant:str):
        """
        Get a menu from a specific restaurant. Return None if there is no menu

        :param restaurant : the restaurant name
        :type restaurant: str
        :return: the menus from the restaurant
        :rtype: List[menu]
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT m.id_menu FROM ensaeats.menu as m "\
                    "WHERE m.nomresto=%(nom)s"
                    , {"nom" : restaurant} )
                res=cursor.fetchall()
        id_menu =[]
        for i in range(len(res)):
            id_menu.append(res[i]['id_menu'])
        return(id_menu)






    def add_menu(self, menu: Menu)-> bool:
        created=False
        id_menu = MenuDao().find_id_by_menuname(menu.nom)
        if id_menu is not None :
            return(created) 

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                ##creer le menu
                cursor.execute(
                    "INSERT INTO ensaeats.menu "\
                    " (nom_menu, prix, nomresto) VALUES "\
                    "(%(nom)s, %(prix)s, %(restaurant)s)"\
                    "RETURNING id_menu"
                , {
                   "nom": menu.nom
                  , "prix": menu.prix
                  , "restaurant": menu.id_restaurant})
                idm = cursor.fetchone()['id_menu']
                #partie des ajoues de plat
        id_conserve = []
        for p in range(len(menu.listplat)) :
            a = DishDao()
            result = a.add_dish(menu.listplat[p])
            id_conserve.append(result)

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
               #ajoue des menu_plat
                for pla in range(len(id_conserve)) :
                    cursor.execute(
                    "INSERT INTO ensaeats.menu_plat "\
                    " (id_menu, id_plat) VALUES "\
                    "(%(m)s, %(p)s)"\
                , {
                   "m": idm
                  , "p": id_conserve[pla]
                  })

                ##ajoue des plat dans 
        created = True
        return (created)

    def update_price_menu(self,nom,newprice):
        id_menu = MenuDao().find_id_by_menuname(nom)
        updated = False
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE ensaeats.menu SET "
                    " prix = %(newprice)s "
                    " where id_menu = %(id_menu)s" , {"newprice" : newprice,'id_menu': id_menu}
                )
        if cursor.rowcount:
                    updated = True
        return updated

    
    def del_menu(self, id_menu:str)-> bool:
        created=False


        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.menu "\
                    "WHERE id_menu = %(id_key)s", {
                   "id_key": id_menu
                 
                  })
                res = cursor.fetchone()
        created = True
        return (created)
    def delete_a_dish_from_a_menu(self, nom_plat,nom_menu) :
        id_plat = DishDao().find_id_by_dishname(nom_plat)
        id_menu = MenuDao().find_id_by_menuname(nom_menu)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                "DELETE FROM ensaeats.menu_plat as mp "
                "WHERE mp.id_menu = %(id_m)s "
                " AND md.id_plat = %(id_p)s",{"id_m":id_menu,"id_p" : id_plat})

