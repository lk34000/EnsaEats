from pydantic.main import BaseModel
from datetime import *


class Commande(BaseModel):
     username : str
     id_restaurant : str
     date : str
     contenu : list = []
