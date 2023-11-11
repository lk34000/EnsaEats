import requests

class RestaurantAppliClient :
    @staticmethod
    def get_restaurant_by_id(id):
        ''' fonction qui à partir d'un id renvoie un restaurant'''
        link = "http://localhost/restaurants/" + id
        response = requests.get(link) 
        return(response.json())

    @staticmethod
    def get_recherche_restaurant_search(username : str, mdp : str ,term : str):
        term1 = term.split(" ")
        term2 = "%20".join(term1)
        term3 = term2.split("&")
        term4 = "%26".join(term3)
        link = 'http://localhost/restaurants/search?username={0}&mdp={1}&term={2}'.format(username,mdp,term4)
        response = requests.get(link)
        return(response.json())

    @staticmethod
    def get_restaurant_autour_de_toi(username : str,mdp : str):
        ''' fonction qui fait une recherche sans mot-clé autour de chez soi'''
        link = 'http://localhost/restaurants/search?username={0}&mdp={1}'.format(username,mdp)
        response = requests.get(link)
        return(response.json())

    @staticmethod
    def get_all_categories(username : str, mdp : str):
        ''' fonction qui renvoie les catégories d'une recherche prélable (sans mot clé)'''
        link = 'http://localhost/restaurants/search/categorielist?username={0}&mdp={1}'.format(username,mdp)
        response = requests.get(link)
        return(response.json())

    @staticmethod
    def get_restaurant_by_categorie(categorie : str ,username : str, mdp : str):
        ''' obtenir tout les restaurants correspondant à une catégorie'''
        categorie1 = categorie.split(" ")
        categorie2 = "%20".join(categorie1)
        categorie3 = categorie2.split("&")
        categorie4 = "%26".join(categorie3)

        link = 'http://localhost/restaurants/search/categorie?categorie={0}&username={1}&mdp={2}'.format(categorie4,username, mdp)
        response = requests.get(link)
        return(response.json())

    
