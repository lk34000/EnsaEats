from typing import List, Optional
from api.Business_Objects.adresse import Adresse
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.Business_Objects.client import Client
from hashlib import sha512


class ClientDao(metaclass=Singleton):
    def find_all_clients(self, limit: int = 0, offset: int = 0) -> List[Client]:
        """
        Get all clients in the db without any filter

        :param limit: how many clients are requested
        :type limit: int
        :param offset: the offset of the request
        :type offset: int
        """
        request = "SELECT * FROM ensaeats.client"
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

    def find_client_by_id(self, id_client: int) -> Optional[Client]:
        """
        Get an client with a specific id. Return None if there is no client

        :param client-id: the client id
        :type id_client: int
        :return: the client
        :rtype: Optional[client]
        """
        with DBConnection().connection as con:
            with con.cursor() as cur:
                cur.execute(
                    "SELECT client.username, client.nom,client.prenom,client.mdp,adresse.ad_postale,adresse.ville,adresse.code_poste,adresse.pays "
                    "from ensaeats.client as client,ensaeats.adresse as adresse,ensaeats.adresse_client as adresse_client "
                    "WHERE client.id_client=%(id)s"
                    "and client.id_client = adresse_client.id_client  "
                    "and adresse.id_adresse = adresse_client.id_adresse", {"id": id_client})
                res = cur.fetchone()
        
        searched_client = None
        
        if res:
            #creer objet adresse
            searched_adresse = Adresse(rue = res["ad_postale"],ville = res["ville"],codepostal = res["code_poste"],pays = res["pays"])
            searched_client = Client(username = res['username'], 
                nom=res['nom'], prenom=res['prenom'], adresse=searched_adresse, mdp=res["mdp"]
            )

        return searched_client

    def username_in_database(self, username : str ):
        with DBConnection().connection as con:
            with con.cursor() as cur:
                cur.execute(
                    "SELECT * "
                    "FROM ensaeats.client as c "
                    "WHERE c.username = %(use)s",{"use" : username}
                )
                res = cur.fetchone()
            if res :
                return True
            else :
                return False



    def find_client_by_username(self, username: str) -> Optional[Client]:
        """
        Get an client with a specific id. Return None if there is no client

        :param client-id: the client id
        :type id_client: int
        :return: the client
        :rtype: Optional[client]
        """
        with DBConnection().connection as con:
            with con.cursor() as cur:
                cur.execute(
                    "SELECT client.username, client.nom,client.prenom,client.mdp,adresse.ad_postale,adresse.ville,adresse.code_poste,adresse.pays "
                    "from ensaeats.client as client,ensaeats.adresse as adresse,ensaeats.adresse_client as adresse_client "
                    "WHERE client.username=%(use)s"
                    "and client.id_client = adresse_client.id_client  "
                    "and adresse.id_adresse = adresse_client.id_adresse", {"use": username})
                res = cur.fetchone()
        
        searched_client = None
        
        if res:
            #creer objet adresse
            searched_adresse = Adresse(rue = res["ad_postale"],ville = res["ville"],codepostal = res["code_poste"],pays = res["pays"])
            searched_client = Client(username = res['username'], 
                nom=res['nom'], prenom=res['prenom'], adresse=searched_adresse, mdp=res["mdp"]
            )

        return searched_client



    def find_id_by_username(self, username: str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_client FROM ensaeats.client as client "
                    "WHERE client.username = %(use)s", {"use": username})
                res = cursor.fetchone()
        if res:
            return res["id_client"]


    def add_client(self, client: Client) -> bool:
        created = False
        #username Already used

        use = ClientDao().username_in_database(client.username)
        if use is True :
            return created

        # Get the id type
        id_client = ClientDao().find_id_by_username(client.username)
        if id_client is not None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                ##ajoue du client

                cursor.execute(
                    "INSERT INTO ensaeats.client (nom,"
                    " prenom, mdp,username) VALUES "    
                    "(%(nom)s, %(prenom)s,%(mdp)s,%(username)s)"
                    "RETURNING id_client", {"nom": client.nom, "prenom": client.prenom, "mdp": sha512(client.mdp.encode()).hexdigest(),'username' : client.username}
                    
                    
                    )
                idc = cursor.fetchone()['id_client']
                
                ##ajoue de l'adresse
                cursor.execute(
                    "INSERT INTO ensaeats.adresse (ad_postale,"
                    " ville, code_poste,pays) VALUES "
                    "(%(ad_post)s, %(ville)s,%(codepost)s,%(pays)s)"
                    "RETURNING id_adresse", {"ad_post": client.adresse.rue, "ville": client.adresse.ville, "codepost": client.adresse.codepostal,"pays" : client.adresse.pays}
                    )
                ida = cursor.fetchone()['id_adresse']
                
                
                ##ajoue adresse_client
                cursor.execute(
                    "INSERT INTO ensaeats.adresse_client (id_adresse,"
                    " id_client) VALUES "
                    "(%(ad)s, %(cli)s)", {"ad": ida, "cli": idc}
                    )


        created = True
        return created

    def update_client_adresse(self, username: str, newadresse : Adresse) -> bool:
        updated = False
        id_client = ClientDao().find_id_by_username(username)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                
                ###recuperer l'id adresse du client
                cursor.execute(
                    "SELECT ac.id_adresse"
                    " FROM ensaeats.adresse_client as ac"
                    " WHERE ac.id_client = %(id_type)s",{"id_type":id_client})
                ida = cursor.fetchone()['id_adresse']

                cursor.execute(
                    "UPDATE ensaeats.adresse SET"
                    " ad_postale = %(adpost2)s"
                    ", ville = %(ville2)s"
                    ", code_poste = %(codep2)s"
                    ", pays = %(pays2)s"
                    " WHERE id_adresse = %(id_adresse)s",{"id_adresse":ida,"adpost2":newadresse.rue,"ville2":newadresse.ville,"codep2":newadresse.codepostal,"pays2":newadresse.pays})



                if cursor.rowcount:
                    updated = True
        return updated
    
    def update_client_password(self, username : str,newmotdepasse :str ):
        updated = False
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE ensaeats.client SET "
                    " mdp = %(mdp)s "
                    " where username = %(us)s" , {'mdp' : sha512(newmotdepasse.encode()).hexdigest(),'us' : username}
                )
        if cursor.rowcount:
                    updated = True
        return updated

        


    def del_client(self, username: str) -> bool:
        created = False

        # Get the id type
        id_key = ClientDao().find_id_by_username(username)
        if id_key is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                ## recuper l'id adresse du client
                cursor.execute(
                    "SELECT ac.id_adresse"
                    " FROM ensaeats.adresse_client as ac "
                    " WHERE ac.id_client = %(id_type)s",{"id_type":id_key})
                ida = cursor.fetchone()['id_adresse']
                
                cursor.execute(
                    "DELETE FROM ensaeats.client as c "
                    "WHERE c.id_client = %(id_key)s",{"id_key":id_key})
                cursor.execute(
                    "DELETE FROM ensaeats.adresse as a "
                    "WHERE a.id_adresse = %(id_a)s",{"id_a":ida})
                cursor.execute(
                    "DELETE FROM ensaeats.adresse_client as ac "
                    "WHERE ac.id_adresse = %(id_a)s and ac.id_client = %(id_c)s",{"id_a":ida,"id_c" : id_key})

        created = True
        return created

    def verifyPassword(self,username : str,mdp :str) -> bool:

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"
                    " FROM ensaeats.client as c "
                    " WHERE c.username = %(use)s"
                    "and c.mdp = %(mdp)s",{"use":username,"mdp" : sha512(mdp.encode()).hexdigest()}
                    )
                cli = cursor.fetchone()

                if cli is None :
                    return False
                else : 
                    return True
    
    