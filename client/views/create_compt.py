import time

from client.api.client_Client import ClientAppliClient 

from PyInquirer import style_from_dict, prompt, Token

#from abstract_views import AbstractView
#from session import Session

class class_creation_de_compte:
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


    def aff_page_create_compt(self) :
        print()
        print("Veuillez remplir les champs, ou entrer <r> pour Revenir à la page d'accueil")

        element_nom = [
                        {
                            'type': 'input',
                            'name': 'nom',
                            'message': '   Nom :',
                        }
                      ]
        choix_nom = prompt(element_nom, style=self.style)
        #---Retour à lHome-----
        if (choix_nom["nom"]=="r") :
            from client.views.main import Home
            return Home().main()
        

        element_prenom = [
                            {
                                'type': 'input',
                                'name': 'prenom',
                                'message': '   Prenom :',
                            }
                        ]
        choix_prenom = prompt(element_prenom, style=self.style)
        #---Retour à lHome-----
        if (choix_prenom["prenom"]=="r") :
            from client.views.main import Home
            return Home().main()

        
        element_username = [
                            {
                                'type': 'input',
                                'name': 'username',
                                'message': '   Username :',
                            }
                        ]
        choix_username = prompt(element_username, style=self.style)
        #---Retour à lHome-----
        if (choix_username["username"]=="r") :
            from client.views.main import Home
            return Home().main()
        stop=True

        while stop==True :
            verif_username = ClientAppliClient.usernameisfree(choix_username['username'])
            good = (len(choix_username['username'].split(" "))==1)
            
            if verif_username == False :
                print()
                print("Désolé, mais cet username existe déja, veuillez en chosir un autre")
                element_username = [
                                        {
                                            'type': 'input',
                                            'name': 'username',
                                            'message': '   Entrer un Username différent :',
                                        }
                                    ]
                choix_username = prompt(element_username, style=self.style)
                if (choix_username["username"]=="r") :
                    from client.views.main import Home
                    return Home().main()
            elif good == False:
                print()
                print("Désolé, mais cet username contient un espace")
                element_username = [
                                        {
                                            'type': 'input',
                                            'name': 'username',
                                            'message': '   Entrer un Username différent :',
                                        }
                                    ]
                choix_username = prompt(element_username, style=self.style)
                if (choix_username["username"]=="r") :
                    from client.views.main import Home
                    return Home().main()

            else:
                stop = False

        print("Bienvenue "+ choix_username["username"] + ". Vous pouvez rentrer votre adresse : ")
        element_num_rue = [
                                {
                                    'type': 'input',
                                    'name': 'adresse_numero_rue',
                                    'message': '   Numero de la rue :',
                                }
                            ]
        choix_num_rue = prompt(element_num_rue, style=self.style)
        #---Retour à lHome-----
        if (choix_num_rue["adresse_numero_rue"]=="r") :
            from client.views.main import Home
            return Home().main()
        

        
        element_rue = [
                            {
                                'type': 'input',
                                'name': 'adresse_rue',
                                'message': '   La Rue :',
                            }
                          ]
        choix_rue = prompt(element_rue, style=self.style)
        #---Retour à lHome-----
        if (choix_rue["adresse_rue"]=="r") :
            from client.views.main import Home
            return Home().main()

        
        element_codpostal = [
                        {
                            'type': 'input',
                            'name': 'adresse_code_postal',
                            'message': '   Le code postal :',
                        }
                      ]
        choix_codpostal = prompt(element_codpostal, style=self.style)

        #---Retour à lHome-----
        if (choix_codpostal["adresse_code_postal"]=="r") :
            from client.views.main import Home
            return Home().main()

        
        element_ville = [
                            {
                                'type': 'input',
                                'name': 'adresse_ville',
                                'message': '   La Ville :',
                            }
                        ]
        choix_ville = prompt(element_ville, style=self.style)
        #---Retour à lHome-----
        if (choix_ville["adresse_ville"]=="r") :
            from client.views.main import Home
            return Home().main()

        print("Vous pouvez renseigner votre mot de passe : ")
        element_mdp_1 = [
                            {
                                'type': 'password',
                                'name': 'password_1',
                                'message': '   Mot de passe :'
                            }
                        ]
        choix_mdp_1 = prompt(element_mdp_1, style=self.style)
        #---Retour à lHome-----
        if (choix_mdp_1["password_1"]=="r") :
            from client.views.main import Home
            return Home().main()
        motdepass_1 = choix_mdp_1["password_1"]
        stop = True
        while stop == True :
            #---Vérifier si le mot de passe ne comporte pas de caractère indésirable---#
            for x in motdepass_1:
                if x in "^'(?=.*_-)?[]\$!%#\"&+/§{,}; " :
                    print('Entrer un mot de passe valide')
                    element_mdp_1 = [
                                        {
                                            'type': 'password',
                                            'name': 'password_1',
                                            'message': '   Password :'
                                        }
                                    ]
                    choix_mdp_1 = prompt(element_mdp_1, style=self.style)
                    #---Retour à lHome-----
                    if (choix_mdp_1["password_1"]=="r") :
                        from client.views.main import Home
                        return Home().main()
                else:
                    stop = False


        element_mdp_2 = [
                            {
                                'type': 'password',
                                'name': 'password_2',
                                'message': '   Confirmez votre mot de passe :'
                            }
                        ]
        choix_mdp_2 = prompt(element_mdp_2, style=self.style)
        #---Retour à lHome-----
        if (choix_mdp_2["password_2"]=="r") :
            from client.views.main import Home
            return Home().main()
        
        stop = True

        while stop == True :
            if choix_mdp_2["password_2"] != choix_mdp_1["password_1"] :
                stop=True
                print("Désolé, mais les deux mots de passes ne sont pas identiques")
                elements_3= [
                                {
                                    'type': 'password',
                                    'name': 'password_1',
                                    'message': "   mot de passse :"
                                },
                                {
                                    'type': 'password',
                                    'name': 'password_2',
                                    'message': "    Confirmez votre mot de passe :"
                                }
                            ]
                mdp = prompt(elements_3, style=self.style)
                choix_mdp_1["password_1"] = mdp["password_1"]
                choix_mdp_2["password_2"] = mdp["password_2"]
            else:
                stop = False
        
        #---------Redirection vers la page de sauvegarde des informations --------#
        ClientAppliClient.new_client( 
                                            choix_username["username"] ,
                                            choix_nom["nom"] ,
                                            choix_prenom["prenom"] ,
                                            str(choix_num_rue["adresse_numero_rue"] +" "+ choix_rue["adresse_rue"]) ,
                                            choix_ville["adresse_ville"] ,
                                            choix_codpostal["adresse_code_postal"] ,
                                            choix_mdp_1["password_1"] , 
                                            pays = 'France'
                                        )

        print("Bravo, votre compte à bien été crée.")
        print()
        time.sleep(2)
        print("Vous serez rédirigé vers la page d'accueil pour procéder à votre authentification")
        time.sleep(3)
        print("\n")
        from client.views.main import Home
        Home().main()
