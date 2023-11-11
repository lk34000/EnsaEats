from fastapi import APIRouter, Header, HTTPException
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
from api.exception.no_restaurants_exception import NorestaurantsSearchException
from api.services.restaurant_services import RestaurantServices
router = APIRouter()

@router.get("/restaurants/search", tags=["restaurants"])
def get_restaurant_by_search(username : str, mdp : str ,term : str = None):
    try:
        recherche = RestaurantServices.search(username = username,mdp = mdp,term = term)
        return(recherche)
    except NorestaurantsSearchException:
        raise HTTPException(status_code=404, detail="Pas de restaurants dans la recherche")
    except ClientNotAuthenticated:
        raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")



@router.get("/restaurants/{id}", tags=["restaurants"])
def get_restaurant_by_id(id:str):
        ressource = RestaurantServices.byid(id)
        return ressource


@router.get("/restaurants/search/categorielist", tags=["restaurants"])
def get_allcategories(username : str, mdp : str, term : str = None):
        try :
            ressource = RestaurantServices.listofcategories(RestaurantServices.search(username,mdp,term))
            return ressource
        except ClientNotAuthenticated:
            raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")


@router.get("/restaurants/search/categorie", tags=["restaurants"])
def get_restaurant_by_categorie(categorie:str,username : str, mdp : str, term : str = None):
        try :
            ressource = RestaurantServices.restaurantcategories(categorie,RestaurantServices.search(username,mdp,term))
            return ressource
        except ClientNotAuthenticated:
            raise HTTPException(status_code=401, detail="Le client n'est pas authentifié")