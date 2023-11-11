from pydantic.main import BaseModel

class Menu(BaseModel):
    nom : str
    idrestaurant : str
    prix : float
    listplat : list
                    

                



# deux menus peuvent pas avoir le même nom, un nom est 
