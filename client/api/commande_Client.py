import requests
class CommandeAppliClient :
    @staticmethod
    def new_commande(username : str,id_restaurant : str):
        link = 'http://localhost/commandes/?username={0}&idrestaurant={1}'.format(username,id_restaurant)
        response = requests.post(link)
        return(response.json())
        

    @staticmethod
    def add_menu(menuname : str,username : str,id_restaurant : str,date : str,contenu : str):
        link = 'http://localhost/commandes/ajoutmenu?menuname={0}'.format(menuname)
        parameters = {
        "username": username,
        "id_restaurant": id_restaurant,
        "date": date,
        "contenu": contenu
        }
        response = requests.put(url = link, json = parameters)
        return(response.json())

    @staticmethod
    def del_menu(menuname : str, username : str, id_restaurant : str, date : str, contenu : list):
        link = 'http://localhost/commandes/supprmenu?menuname={}'.format(menuname)
        parameters = {
        "username": username,
        "id_restaurant": id_restaurant,
        "date": date,
        "contenu": contenu
        }
        response = requests.delete(url = link, json = parameters)
        return(response.json())

    @staticmethod
    def consult_prices(username : str, id_restaurant : str, date : str, contenu : list):
          link = 'http://localhost/commandes/prix'
          parameters = {
            "username": username,
            "id_restaurant": id_restaurant,
            "date": date,
            "contenu": contenu
            }
          response = requests.post(url = link, json = parameters)
          return(response.json())

    @staticmethod
    def consult_content(username : str, id_restaurant : str, date : str, contenu : list):
          link = 'http://localhost/commandes/consulter'
          parameters = {
            "username": username,
            "id_restaurant": id_restaurant,
            "date": date,
            "contenu": contenu
            }
          response = requests.post(url = link, json = parameters)
          return(response.json())

    @staticmethod
    def register_order(username : str, id_restaurant : str, date : str, contenu : list, mdp : str):
        link = 'http://localhost/commandes/enregistre?mdp={}'.format(mdp)
        parameters = {
            "username": username,
            "id_restaurant": id_restaurant,
            "date": date,
            "contenu": contenu
            }   
        response = requests.post(url = link, json = parameters)
        

          




