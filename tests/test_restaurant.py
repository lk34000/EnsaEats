import unittest
from api.services.restaurant_services import RestaurantServices
from pydantic.types import NonNegativeFloat
from api.Business_Objects.restaurant import Restaurant
from api.Business_Objects.client import Client
from api.Business_Objects.adresse import Adresse
from typing import List

class TestRestoServices(unittest.TestCase):
    def __init__(self, methodName) -> None:
        super().__init__(methodName=methodName)
        self.r = Restaurant(nom='Le Tandoor', type=['Indian'], adresse=Adresse(rue='42 Rue De L Horloge', ville='Sedan', codepostal='08200', pays='FR'), id_restaurant='k4GPALyPGdE5lvNF8nKLaQ', notemoyenne=4, est_ouvert=True, menus_proposés=[])
        self.c = Client(username = "souventblesse",nom = 'Guniore',prenom = 'Naimarre',adresse= Adresse(rue = '1 ruelle des vignes',ville = 'Balan',codepostal = '08200',pays = 'France'),mdp = 'dobrasil')
        #self.rech est la recherche pour le client Naimarre Guniore, habitant a Sedan, voulant un restaurant indien. Il n'y en a qu'un seul, le restaurant Le Tandoor, mis dans le constructeur de la classe de test
        self.rech = RestaurantServices().search(self.c.username,self.c.mdp,"Indian")

    def test_recherchebyid(self): 
        self.assertEqual(self.r,RestaurantServices().byid(self.r.id_restaurant))

    def test_recherche(self):
        #recherche pour le client Naimarre Guniore, habitant a Sedan, voulant un restaurant indien. Il n'y en a qu'un seul, le restaurant Le Tandoor, mis dans le constructeur de la classe de test
        #ici, on convertit le restaurant en liste de restaurant car la méthode search renvoie une liste
        self.assertEqual([self.r],self.rech)
    
    def test_liste_categorie(self):
        #test sur la recherche des catégories de restaurant contenus dans la recherche de la méthode précédente : il y'a seulement la catégorie indien
        self.assertEqual(self.r.type,RestaurantServices().listofcategories(self.rech))
    
    def test_resto_categorie(self):
        #test sur la recherche de restaurant indien parmi les restaurants recherchés auparavant
        self.assertEqual([self.r],RestaurantServices().restaurantcategories("Indian",self.rech))

if __name__ == '__main__':
    unittest.main()

