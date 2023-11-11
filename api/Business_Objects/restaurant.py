from datetime import *
from pydantic.main import BaseModel
from api.Business_Objects.adresse import Adresse

class Restaurant(BaseModel):
    nom : str
    type : list
    adresse : Adresse
    id_restaurant : str
    notemoyenne : int
    est_ouvert : bool = False
    menus_proposés : list = []
