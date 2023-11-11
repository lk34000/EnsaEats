import requests


class ClientAppliClient:
        @staticmethod
        def new_client(username : str,nom : str,prenom : str,rue : str,ville : str,codepostal : str , mdp : str, pays = 'France'):
            parameters = {
            "username": username,
            "nom": nom,
            "prenom": prenom,
            "adresse": {
            "rue": rue,
            "ville": ville,
            "codepostal": codepostal,
            "pays": pays},
            "mdp": mdp,
            "historique_commande" : []}
            response = requests.post(url = 'http://localhost/clients/', json = parameters)
            return(response)


        @staticmethod
        def modifypassword(username : str, mdp : str,newmdp : str):
         link = 'http://localhost/clients/updatemdp?username={0}&mdp={1}&newmdp={2}'.format(username,mdp,newmdp)
         response = requests.put(link)
         return(response.json())
         
        @staticmethod
        def modifyadress(username : str , mdp : str, rue : str, codepostal : str,ville : str , pays : str = "France" ) : 
            link ='http://localhost/clients/updateadress?username={0}&mdp={1}&rue={2}&codepostal={3}&ville={4}&pays={5}'.format(username,mdp,rue,codepostal,ville,pays)
            response = requests.put(link)
            return(response.json())
            
        @staticmethod
        def authentification(username : str , mdp :str) : 
            link = "http://localhost/clients/authentification?username={0}&mdp={1}".format(username,mdp)
            response = requests.get(link)
            return(response.json())
        
        @staticmethod
        def order_history(username : str, mdp :str):
            link = "http://localhost/clients/historiquecommande?username={0}&mdp={1}".format(username,mdp)
            response = requests.get(link)
            return(response.json())

        @staticmethod
        def usernameisfree(username : str) : 
            link =  'http://localhost/clients/usernamefree?username={0}'.format(username)
            response = requests.get(link)
            return(response.json())

