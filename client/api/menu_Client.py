import requests
class MenuAppliClient :
    
    @staticmethod
    def get_menus(idrestaurant : str):
        link = 'http://localhost/menus/?idrestaurant={0}'.format(idrestaurant)
        reponse = requests.get(link)
        return(reponse.json())

    

