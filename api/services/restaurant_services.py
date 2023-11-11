from pydantic.types import NonNegativeFloat
from api.API.Connect_API import API
from api.exception.no_restaurants_exception import NorestaurantsSearchException
from api.services.client_service import Clientservice
from api.services.converter_services import ConverterServices
from api.Business_Objects.client import Client
from api.Business_Objects.adresse import Adresse
from typing import List


class RestaurantServices:
    ''' This class allows you to search for restaurants
          It has 4 methods which are
           - byid or search by identifier which returns a restaurant object
           - search which allows from a customer (and his location) and a keyword (what he is looking to eat for example)
           to return a list of restaurants by distance, the customer will then choose one of these restaurants according to his choice
           
            The following methods use the results of the previous searches, the first listofcategories returns the list of categories
            of a search, so that the user has a list of categories in front of him if he doesn't know what to choose 
            A last method is a method that from a category returns the list of restaurants around you associated, we will use this method after a search around you


           RestaurantServices uses the ConverterServices class which converts the Yelp json results into a Restaurant object.
    '''
    @staticmethod
    def byid(id : str):
          '''Do a search knowing the id of the restaurant chosen '''
          objet = API()
          res = objet.connect_id(id)
          return(ConverterServices(res).method())

    @staticmethod
    def search(username : str, mdp : str, term : str = None):
            ''' do a keyword search using at least the client's location'''
            objet = API()
            categories = 'Restaurants'
            sort_by = 'distance'
            client = Clientservice.authentification_and_get_client(username,mdp)
            location = client.adresse.rue + "," + client.adresse.ville + "," + client.adresse.pays
            if term == None :
              params = {
                'location': location.replace(' ', '+'),
                'categories':categories.replace(' ', '+'),
                'sort_by': sort_by.replace(' ', '+'),
                'limit': 15
                }
            if term != None :
                 params = {
                'term': term.replace(' ','+'),
                'location': location.replace(' ', '+'),
                'categories':categories.replace(' ', '+'),
                'sort_by': sort_by.replace(' ', '+'),
                'limit': 15
                }
            res = objet.connect_search(params)
            l = []
            for x in res['businesses']:
                l.append(ConverterServices(x).method())
            if l != []:
                return(l)
            else:
                raise NorestaurantsSearchException

    
    @staticmethod
    def listofcategories(l : list):
          ''' Return the list of categories of the associated search'''
          res = []
          for x in l :
                for j in x.type:
                      res.append(j)
          return(list(dict.fromkeys(res)))


    @staticmethod
    def restaurantcategories(categorie : str, search : list):
          ''' From a search made beforehand and a category chosen by the customer:  return all corresponding restaurants'''
          res = []
          for restaurant in search:
              for i in restaurant.type:
                  if i == categorie:
                        res.append(restaurant)
          return(res)

        



                
                      

      
    
      
      
            







##exemple Restaurant par ID
a = RestaurantServices()
#print(a.byid(id = 'AdDVKcyQxd6ZI6PzadQbSA'))

## exemple restaurant par recherche
exadresse = Adresse(rue = '4 rue louis Armand',ville ='Bruz',codepostal ='35170')
exclient = Client(username = 1896,nom = 'Pain', prenom = 'Guillaume', adresse = exadresse, mdp = 'jadorenabilfekir')
#Guillaume recherche un restaurant de Pizzas
#recherche = RestaurantServices.search(username = 'test',mdp = 'test', term = 'pizza')
#print(recherche)
#parmi les restaurants proposés à Guillaume dans sa dernière recherche on veut toutes les catégories
#print(RestaurantServices.listofcategories(recherche))


# je veux voir les restaurants de burgers proposés a guillaume
#print(RestaurantServices.restaurantcategories('Burgers',recherche))






## soit tu cherches autour de chez toi, soit de quoi avez vous envie
# si tu cherches de quoi avez vous envie tu as besoin que d'un term et on renvoie une liste de restaurants
# sinon autour de chez toi tu vas avoir une option "par catégorie" et on propose au client une liste de catégories

# il faut donc faire une fonction qui détermine toutes les catégories d'une recherche puis une fonction qui à partir d'une catégorie renvoie tout les restaurants de la recherche

