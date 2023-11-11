from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from api.Business_Objects.adresse import Adresse
from api.Business_Objects.client import Client
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
from api.services.client_service import Clientservice
router = APIRouter()

@router.post("/clients/", tags=["clients"])
def create_client(client: Client):
    return Clientservice.new_client(client)


@router.put("/clients/updatemdp", tags=["clients"])
def update_password(username : str, mdp : str,newmdp : str):
    try : 
        client = Clientservice.authentification_and_get_client(username,mdp)
        Clientservice.updateclientpassword(username = username, mdp = newmdp)
    except ClientNotAuthenticated(username = username):
         raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")


@router.put("/clients/updateadress", tags=["clients"])
def update_adress(username : str, mdp : str, rue : str, codepostal : str, ville : str, pays : str = 'France'):
    try : 
        client = Clientservice.authentification_and_get_client(username,mdp)
        Clientservice.updateclientadresse(username = username, newadresse = Adresse(rue = rue, ville = ville, codepostal = codepostal, pays = pays))
    except ClientNotAuthenticated(username = username):
         raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")

@router.get("/clients/authentification", tags = ["clients"])
def authentification_and_get_client(username : str ,mdp : str):
    try :
        client = Clientservice.authentification_and_get_client(username,mdp)
        return(client)
    except ClientNotAuthenticated(username = username):
         raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")


@router.get("/clients/usernamefree", tags = ["clients"])
def username_is_free(username : str):
    return(Clientservice.usernameisfree(username))

@router.get("/clients/historiquecommande",tags=["clients"])
def order_history(username : str,mdp : str) : 
    try : 
        client = Clientservice.authentification_and_get_client(username,mdp)
        return(Clientservice.find_order_by_username(username=username))
    except ClientNotAuthenticated(username = username):
         raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")

