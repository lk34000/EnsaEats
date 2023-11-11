from api.Business_Objects.plat import Plat
from api.dao.menu_dao import MenuDao
from api.dao.dish_dao import DishDao

class DishServices:
    @staticmethod
    def add_dish_dao(dish : Plat):
        return(DishDao().add_dish(dish))

    @staticmethod
    def del_dish_menu(dish_name : str, menuname : str ):
        return(MenuDao().delete_a_dish_from_a_menu(dish_name,menuname))


        


