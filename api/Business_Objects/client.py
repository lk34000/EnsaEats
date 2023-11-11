from api.Business_Objects.adresse import Adresse

from pydantic import BaseModel
from api.Business_Objects.adresse import Adresse

class Client(BaseModel):
    username : str
    nom : str
    prenom : str
    adresse : Adresse
    mdp : str
    historique_commande : list = []


## verifier tout les objets métiers, ensuite vérifier que les fonctions services fonctionnent avec ces objets métiers puis tester les routers de l'API



