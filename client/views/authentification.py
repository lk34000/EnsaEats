from PyInquirer import style_from_dict, prompt, Token
import time
from client.api.client_Client import ClientAppliClient


class Auth:
    def __init__(self) -> None:
        self.style = style_from_dict({
            Token.Separator : '#fff',           #white
            Token.QuestionMark : '#000',        #black
            Token.Selected : '#00BFFF',         #sky blue
            Token.Pointer : '#fff',             #white
            Token.Instruction : '#fff',         #white
            Token.Answer : '#008000 bold',      #green
            Token.Question : '#FF7F50',         #shade of orange
        })


        self.elements_1= [
                            {
                                'type': 'input',
                                'name': 'username',
                                'message': "Nom d'utilisateur :",
                            }
                        ]

        self.elements_2= [
                            {
                                'type': 'password',
                                'name': 'password',
                                'message': "Mot de passe :"
                            }
                        ]

    def auth(self) :
        print()
        print("Veuillez saisir vos identifiants, ou entrer <r> pour Revenir à l'Accueil")
        
        list_choix_1 = prompt(self.elements_1, style=self.style)
        #---Retour à lAccueil-----
        if (list_choix_1["username"]=="r") :
            from client.views.main import Accueil
            return Accueil().main()
        
        list_choix_2 = prompt(self.elements_2, style=self.style)
        #---Retour à lAccueil-----
        if (list_choix_2["password"]=="r") :
            from client.views.main import Home
            return Home().main()

        
        motdepass = list_choix_2["password"]
        stop = True
        while stop :
            #print(motdepass)
            for x in motdepass:
                if x in "^'(?=.*_-)?[]\$!%#\"&+/§{,};" :
                    stop = True
                    break
                else:
                    stop = False

            if stop == True :
                print()
                print('Désolé, mais votre mot de passe comporte un ou plusieurs caractères indésirables.')
                
                elements= [
                            {
                                'type': 'password',
                                'name': 'password',
                                'message': "Veuillez saisir un mot de passe correct. :"
                            }
                        ]
                mdp = prompt(elements, style=self.style)
                #---Retour à lAccueil-----
                if (mdp["password"]=="r") :
                    from client.views.main import Home
                    return Home().main()
                motdepass=mdp["password"]
            
            list_choix_2["password"] = motdepass

        #----Construction des données à retourner---------#
        info_identif_client = {
                                "username" : list_choix_1["username"],
                                "password" : list_choix_2["password"]
                              }   
        
        
        #info_user_auth = ClientDao().verifyPassword(list_choix_1["username"] , list_choix_2["password"])
        auth_client = ClientAppliClient.authentification(username = list_choix_1["username"] ,mdp =  list_choix_2["password"])
        ok = list(auth_client.keys())[0] != 'message'
        
        if ok == True :
            
            #---récupération des informations sur le client cconnecté à paritr de l'id
            info_client = {'username' : auth_client['username'],
                                'nom' : auth_client['nom'],
                                'prenom' : auth_client['prenom'],
                                'adresse' : {'rue' : auth_client['adresse']['rue'],
                                                    'ville' : auth_client['adresse']['ville'],
                                                    'codepostal' : auth_client['adresse']['codepostal'],
                                                    'pays' : auth_client['adresse']['pays']

                                },
                                'mdp' : list_choix_2["password"]

            }
            #redirection vers la page de profil du client
            from client.views.profil_page import Home_profile
            Home_profile().main(info_client)
            
            

        else:
            print('Désolé, mais vos identifiants ou mot de passe sont incorrects.')
            print()
            print("Vous serrez rédirigé vers la page d'Accueil. \n Merci de bien vouloir créer un compte ou de réessayer la connection.")
            print()
            elements = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Ok :',
                                    'choices' : ['Ok']
                                }
                        ]
            list_choix = prompt(elements, style=self.style)
            choix = list_choix["capital"]
            if(choix=='Ok'):
                from client.views.main import Home
                Home().main()



