from typing import List, Optional
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.Business_Objects.plat import Plat


class DishDao(metaclass=Singleton):

    def find_all_dishes(self, limit: int=0, offset: int=0)-> List[Plat]:
        """
        Get all dishes in the db without any filter

        :param limit: how many dishes are requested
        :type limit: int
        :param offset: the offset of the request
        :type offset: int
        """
        request = "SELECT * FROM ensaeats.plat"
        if limit:
            request += f"LIMIT {limit}"
        if offset:
            request += f"OFFSET {offset}"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    request
                )
                res = cursor.fetchall()
        return res
    
    def find_dish_by_menu(self,id_menu : str) :
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    "SELECT mp.id_plat,m.nomresto "
                    "from ensaeats.menu_plat as mp, ensaeats.menu as m"
                    " WHERE mp.id_menu=%(id)s AND mp.id_menu = m.id_menu"
                    , {"id": id_menu})
                res = cursor.fetchall()
            id_r = res[0]['nomresto']

            liste_id_plat = []
            for i in range(len(res)):
                liste_id_plat.append(res[i]['id_plat'])
            
            liste_objet_plat = []
            for i in range(len(liste_id_plat)):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT p.nom_plat "
                        "from ensaeats.plat as p "
                        " WHERE p.id_plat = %(id)s ",
                        {"id": liste_id_plat[i]}
                        )

                    res = cursor.fetchone()

                    nom_plat=res['nom_plat']
                
                objet_plat = Plat(nom = nom_plat, id_restaurant = id_r)

                liste_objet_plat.append(objet_plat)

        return(liste_objet_plat)
    
    


    def find_dish_by_id(self, id_plat: int)-> Optional[Plat]:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    "SELECT * "
                    "from ensaeats.plat as p, ensaeats.menu as m, ensaeats.menu_plat as mp"
                    " WHERE p.id_plat=%(id)s"
                    " and p.id_plat = mp.id_plat"
                    " and mp.id_menu = m.id_menu", {"id": id_plat})
                res = cursor.fetchone()


        searched_dish = None
        if res:
            searched_dish = Plat(
                nom = res['nom_plat'],
                restaurant = res['nomresto']
            )

        return searched_dish

    def add_dish(self,plat : Plat)->bool :
        ceated = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                ##ajoue du plat

                cursor.execute(
                    "INSERT INTO ensaeats.plat (nom_plat) "
                    " VALUES "
                    "(%(nom)s)"
                    " RETURNING id_plat"
                    , {"nom": plat.nom,}
                    )
                idp = cursor.fetchone()['id_plat']
        return(idp)

    def find_id_by_dishname(self,dishname):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT p.id_plat "
                    " from ensaeats.plat as p  "
                    " where p.nom_plat = %(dishname)s",{"dishname": dishname}
                )
                idp = cursor.fetchone()['id_plat']
        return(idp)




