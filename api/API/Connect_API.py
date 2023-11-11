import requests
import urllib
from urllib.error import HTTPError
from urllib.parse import quote

''' Cette classe va être celle qui va nous permettre de nous connecter à l'API de Yelp et de récupérer ensuite ses données
Nous effectuons seulement la requête sans mettre en compte de paramètres, l'objectif de cette classe étant uniquement la connection'''

class API:
    ''' La classe API possède seulement un attribut statut qui sera déterminé lors de la connection
        Nous aurions pu utiliser des attributs host ou path si nous aurions voulu réutiliser ce code pour d'autres Webservices mais nous l'utiliserons en pratique
        juste pour Yelp API.
        Elle possède deux méthodes correspondants aux endpoints que nous utiliserons dans le projet, et une méthode permettant de comprendre le statut du code
        '''
    def __init__(self,statut : str = None):
        self.statut = statut


    def connect_search(self,parameters = None):

      ''' Cette première méthode permet à partir de paramètres de rechercher un restaurant sur la base de données de Yelp
          Les paramètres et les fonctions dessus seront implémentées dans services
          Cette fonction permet alors de se connecter à l'endpoint https://api.yelp.com/v3/businesses/search
      '''
      parameters = parameters or {}
      key = "jTKT7VXQpA2_ovJ98xuWrUvbGrrf2CnKqQUpjHeYZ-N93IsP-HcvvHCctE41ngSp6Ox4xtrOquyVe2xSBiEM7XZYJdrYP834Q_Dm5E-X8j3AlyeR4V1WMeggytlvYXYx "
      url = '{0}{1}'.format('https://api.yelp.com/v3', quote('/businesses/search'.encode('utf8')))
      headers = {
        'Authorization': 'Bearer %s' % key,
      }
      print(u'Se connecte à {0} ...'.format(url))
      res = requests.request('GET', url, headers=headers, params = parameters)
      self.statut = res.status_code
      return (res.json())


    def connect_id(self, id : str = None):

      ''' Cette seconde méthode permet de rechercher un restaurant sur la base de données de Yelp à partir de son identifiant
          Les fonctions dessus seront implémentées dans services
          Cette fonction permet alors de se connecter à l'endpoint https://api.yelp.com/v3/businesses/{id}
      '''
      id = id or ''
      endpoint = '/businesses/' + id
      key = "jTKT7VXQpA2_ovJ98xuWrUvbGrrf2CnKqQUpjHeYZ-N93IsP-HcvvHCctE41ngSp6Ox4xtrOquyVe2xSBiEM7XZYJdrYP834Q_Dm5E-X8j3AlyeR4V1WMeggytlvYXYx "
      url = '{0}{1}'.format('https://api.yelp.com/v3', quote(endpoint.encode('utf8')))
      headers = {
        'Authorization': 'Bearer %s' % key,
      }
      print(u'Se connecte à {0} ...'.format(url))
      res = requests.request('GET', url, headers=headers, params = None)
      self.statut = res.status_code
      return (res.json())


    def statutconnection(self):

        '''Cette méthode permet de savoir si la connection a réussi/échoué et quel est le message d'erreur associé
        Le statuscode associé au module resquests ne renvoyant uniquement un code ceci peut être utile pour comprendre plus rapidement des erreurs
        '''
        a = self.statut
        if a == 200:
            return("tout s'est bien passé")
        if a == 201:
            return("ressource crée avec succès")
        if a == 202:
            return("requête acceptée, sans garantie du résultat")
        if a == 400:
            return("erreur de syntaxe dans la requête")
        if a == 403:
            return("ressource interdite (droits)")
        if a == 401:
            return("erreur, authentification nécessaire")
        if a == 404:
            return("ressource non trouvée")
        if a == 405:
            return("une mauvaise méthode http a été utilisée")
        if a == 500:
            return("erreur côté serveur")
        if a == 503:
            return("service temporairement indisponible")
        if a == None:
            return("Connectez vous d'abord à l'API avant de demander le statut")
        else:
            return(a + "un résultat 2XX indique un succès, un résultat 4XX ou 5XX une erreur")
    

 