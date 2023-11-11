from typing import List, Optional
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.Business_Objects.adresse import Adresse
from api.Business_Objects.menu import Menu



class AdresseDao(metaclass=Singleton):

    def find_all_addresses(self, limit: int=0, offset: int=0)-> List[Adresse]:
        request= "SELECT * FROM adresse"
        if limit :
            request+=f"LIMIT {limit}"
        if offset :
            request+=f"OFFSET {offset}"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                )
                res = cursor.fetchall()
        return res

    def find_address_by_id(self, idadresse: int)-> Optional[Adresse]:
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT * from adresse "\
                        "WHERE id_menu=%(id)s"
                    , {"id" : idadresse})
                    res = cursor.fetchone()
        searched_menu = None

        if res :
            searched_menu = Menu(
            numerorue=res['numerorue']
                , rue=res['rue']
                , codepostal=res['codepostal']
                , id_adresse=res['id_adresse']
                , pays=res['pays']
                , ville=res['ville']
                )

        return (searched_menu)




