from api.Business_Objects.adresse import Adresse
from api.dao.order_dao import OrderDao
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
from api.Business_Objects.client import Client
from api.dao.client_dao import ClientDao


class Clientservice:

    @staticmethod
    def new_client(client: Client) -> bool:
        return ClientDao().add_client(client)

    @staticmethod
    def updateclientpassword(username: str, mdp: str) -> bool:
        return ClientDao().update_client_password(username,mdp)

    @staticmethod
    def updateclientadresse(username: str, newadresse: Adresse) -> bool:
        return ClientDao().update_client_adresse(username,newadresse) 
    

    @staticmethod
    def deleteclient(username: str) -> bool:
        return ClientDao().del_client(username)

    @staticmethod
    def authentification_and_get_client(username: str, mdp: str):
        if (ClientDao().verifyPassword(username, mdp)):
            return ClientDao().find_client_by_username(username)
        else:
            return ClientNotAuthenticated(username=username)

    @staticmethod
    def usernameisfree(username : str):
        if ClientDao().username_in_database(username)== False:
            return(True)
        else :
            return(False)


    @staticmethod
    def find_order_by_username(username) :
        return(OrderDao().find_order_by_username(username=username))
