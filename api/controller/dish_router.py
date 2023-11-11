from fastapi import APIRouter
from api.Business_Objects.plat import Plat

from api.services.dish_services import DishServices


router = APIRouter()


@router.post("/plats/add", tags = ["plats"])
def add_dishs(plat : Plat):
    return(DishServices.add_dish_dao(plat))

@router.delete("/plats/del", tags = ["plats"])
def del_dish_from_menu(menuname : str, platname : str):
    return(DishServices.del_dish_menu(platname,menuname))

