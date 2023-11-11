from typing import List, Optional
from api.dao.client_dao import ClientDao
from api.dao.menu_dao import MenuDao
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.Business_Objects.commande import Commande



class OrderDao(metaclass=Singleton):

    def find_all_orders(self, limit: int=0, offset: int=0)->List[Commande]:
        """

        Get all orders in the db without any filter

        :param limit: how many orders are requested
        :type limit: int
        :param offset: the offset of the request
        :type offset: int
        """
        request="SELECT * FROM commande"
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

    def find_order_by_id(self, idcommande: int)-> Optional[Commande]:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * from ensaeats.commande "
                    "WHERE id_commande=%(id)s", {"id": idcommande})
                res = cursor.fetchone()
        searched_order = None

        if res:
            searched_order= Commande(
                client=res['client'], restaurant=res['restaurant'], date=res['date'], statut=res["statut"], id_commande=res['id_commande'], prix=res['prix'], contenu=res['contenu']
            )

        return searched_order
    
    def add_order(self,commande : Commande) :
        #check whether the menus belong to the same restaurant
        created = False
        menu_resto = MenuDao().find_id_menu_by_restaurant(commande.id_restaurant)
        check = all(item in menu_resto for item in commande.contenu)
        if check == False :
            return(created)

        ##trouver le prix d'une commande
        prix = 0
        for menu in range(len(commande.contenu)) :
           prix += MenuDao().find_price_by_id_menu(commande.contenu[menu])

        ## trouver l'id du client
        id_client = ClientDao().find_id_by_username(commande.username)
        print(id_client)
        with DBConnection().connection as connection:
            ## partie ajoue d'une commande
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.commande "
                    "(id_client , nom_restaurant , date , prix) "
                    " VALUES "
                    " (%(idc)s,%(idr)s,%(date)s,%(prix)s)"
                    "RETURNING id_commande" ,
                    {'idc' : id_client, 'idr' : commande.id_restaurant, 'date' :commande.date,'prix' : prix}
                )
                res = cursor.fetchone()['id_commande']

                output = []
                for x in commande.contenu:
                    if x not in output:
                         output.append(x)
                ##ajoue des contenu_commande
                for i in range(len(output)):
                    quantite = commande.contenu.count(output[i])
                    cursor.execute(
                        "INSERT INTO ensaeats.contenu_commande "
                        " (id_commande,id_menu,quantite)"
                        " VALUES "
                        " (%(idc)s,%(idm)s,%(quanti)s)",{'idc' : res,'idm' : output[i],'quanti' : quantite}
                    )
        created = False
        return(created)
                


    def find_order_by_username(self,username) :
        id_client = ClientDao().find_id_by_username(username)

        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                ###commande d'un id
                cursor.execute(
                    "SELECT * "
                    "FROM ensaeats.commande as c "
                    "WHERE c.id_client = %(idc)s",{"idc" : id_client}
                )
                com = cursor.fetchall()
                ## commande ?
                if(len(com)==0):
                    return("no order for this customer")


        

                ###liste d'objet commande
        liste_commande = []
        #boucle par commande
        for co in range(len(com)):
            commande_ligne = com[co]
            #id_resto
            idr = commande_ligne['nom_restaurant']
            #date
            d =  commande_ligne['date']
            #liste d'objet menu
            id_commande = commande_ligne['id_commande']
            ##recuper les id_menu des commandes
            with DBConnection().connection as connection :
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT * "
                        "FROM ensaeats.contenu_commande as cc "
                        "where cc.id_commande = %(idc)s", {"idc" : id_commande}
                    )
                    m = cursor.fetchall()
                    #nombre de menu :
            cont =[]
            for me in range(len(m)) : 
                ligne = m[me]
                quanti=ligne['quantite']
                for i in range(quanti) :
                    cont.append(MenuDao().find_menu_by_id(ligne['id_menu']))

            liste_commande.append(Commande(username = username , id_restaurant = idr, date = str(d),contenu = cont))
        return(liste_commande)
        
    def find_order_by_restaurant(self,id_restaurant) :
        ###chercher toute les commandes de cette id_restaurant
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * "
                    "FROM ensaeats.commande as c "
                    " WHERE c.nom_restaurant = %(idr)s ",{'idr' : id_restaurant}
                )
                m = cursor.fetchall()
        hist_commande_resto = []
        for com in range(len(m)):
            commande = m[com]
            
            username = ClientDao().find_client_by_id(m[com]['id_client']).username
            idr = id_restaurant
            date = m[com]['date']
            numero_commande = m[com]["id_commande"]
            with DBConnection().connection as connection :
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT * "
                        "FROM ensaeats.contenu_commande as cc "
                        "where cc.id_commande = %(idc)s", {"idc" : numero_commande}
                    )
                    lm = cursor.fetchall()
                    #nombre de menu :
            cont =[]
            for me in range(len(lm)) : 
                ligne = lm[me]
                quanti=ligne['quantite']
                for i in range(quanti) :
                    cont.append(MenuDao().find_menu_by_id(ligne['id_menu']))

            hist_commande_resto.append(Commande(username = username,id_restaurant=idr,date=str(date),contenu = cont))
        return(hist_commande_resto)



