from fastapi import APIRouter
from api.Business_Objects.menu import Menu


from api.services.menu_service import MenuServices


router = APIRouter()


@router.get("/menus/", tags = ["menus"])
def get_menus(idrestaurant : str):
    return(MenuServices.get_menus(idrestaurant))

@router.post("/menus/add", tags = ["menus"])
def add_menus(menu : Menu):
    return(MenuServices.add_menu_dao(menu))

@router.put("/menus/price", tags = ["menus"])
def change_price_menu(menu : Menu, newprice : float):
    return(MenuServices.changeprix_menu(menu,newprice))

@router.delete("/menus/del", tags = ["menus"])
def del_menus(menu : Menu):
    return(MenuServices.del_menu_dao(menu))
