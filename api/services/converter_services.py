from os import name
from api.Business_Objects.restaurant import Restaurant
from api.Business_Objects.adresse import Adresse
from api.dao.menu_dao import MenuDao

class ConverterServices :
    '''This class will convert a dictionary (what the Yelp API returns) into a restaurant object  
    '''
    def __init__(self,res : dict):
        self.res = res

    def method(self): 
          nom = self.res['name']
          est_ouvert =  not(self.res['is_closed'])
          id_restaurant = self.res['id']
          notemoyenne = self.res['rating']
          type = []
          for i in self.res['categories']:
              type.append(i['title'])
          rue = 'no adress'
          if self.res['location']['address1']!= None:
                rue = self.res['location']['address1']
                if self.res['location']['address2'] != None:
                    rue =  rue + self.res['location']['address2']
                    if self.res['location']['address3'] != None:
                        rue = rue + self.res['location']['address2']
          codepostal = self.res['location']['zip_code']
          pays = self.res['location']['country']
          ville = self.res['location']['city']
          adresse = Adresse(rue = rue,ville = ville,codepostal = codepostal,pays = pays)
          menus_proposés = MenuDao().find_menu_by_restaurant(id_restaurant)
          Restaurantfinal = Restaurant(nom = nom,type = type, adresse = adresse,id_restaurant = id_restaurant, notemoyenne =notemoyenne, est_ouvert = est_ouvert, menus_proposés = menus_proposés)
          return(Restaurantfinal)


# pour les if avec les adresses, ceci est du à certains manques d'adresses sur des restaurants de Yelp

