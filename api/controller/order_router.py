from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from api.Business_Objects.commande import Commande
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
from api.services.client_service import Clientservice
from api.services.order_services import OrderServices
router = APIRouter()


@router.post("/commandes/", tags = ['commandes'])
def new_order(username : str, idrestaurant : str):
    return(OrderServices.new_order(username,idrestaurant))

@router.put("/commandes/ajoutmenu", tags = ['commandes'])
def add_menu(commande : Commande,menuname : str):
    return(OrderServices.add_menu(commande,menuname))

@router.delete("/commandes/supprmenu", tags = ['commandes'])
def delete_menu(commande : Commande ,menuname : str):
    return(OrderServices.delete_menu(commande,menuname))

@router.post("/commandes/prix", tags = ["commandes"])
def consult_prices(commande : Commande):
    return(OrderServices.consult_prices(commande))

@router.post("/commandes/consulter", tags = ['commandes'])
def consult_order(commande : Commande):
    return(OrderServices.consult_order(commande))

@router.post("/commandes/enregistre", tags = ["commandes"])
def register_order(commande : Commande, mdp : str):
    try : 
      client = Clientservice.authentification_and_get_client(commande.username,mdp)
      return(OrderServices.register_order(commande))
    except ClientNotAuthenticated:
         raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")

@router.get('/commandes/{idrestaurant}', tags = ["commandes"])
def restaurant_orders(idrestaurant : str):
    pass # à faire
