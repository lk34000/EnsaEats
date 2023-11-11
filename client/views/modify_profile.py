import time
from client.api.client_Client import ClientAppliClient
from PyInquirer import style_from_dict, prompt, Token


class Modify_information:
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


    def display_page_change_account(self, info_client) :
        print()
        print("Modifier les informations")

        choix_modif = [
                            {
                                'type' : 'list',
                                'name' : 'capital',
                                'message' : '',
                                'choices' : ['Modifier mot de passe','Modifier adresse','Voir infos actuelles', 'Retour']
                            }
                        ]
        choix_modif2 = prompt(choix_modif, style=self.style)

        if (choix_modif2["capital"]=='Retour') :
            from client.views.profil_page import Home_profile
            return Home_profile().main(info_client)
        
        if(choix_modif2["capital"]=='Voir infos actuelles'):
            print("Voici vos informations actuelles")
            print("username : " + info_client['username'])
            print("Prenom Nom : " + info_client['prenom'] + " " + info_client['nom'])
            print("Adresse : "  + info_client['adresse']['rue'] + " " + info_client['adresse']['codepostal'] + " " + info_client['adresse']['ville'] + " " + info_client['adresse']['pays'])
            elements = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Faire retour :',
                                    'choices' : ['Retour']
                                }
                        ]
            list_choix = prompt(elements, style=self.style)
            choix = list_choix["capital"]
            if(choix=='Retour'):
                return Modify_information().display_page_change_account(info_client)

        
        if (choix_modif2["capital"]=="Modifier mot de passe") :
            element_mdp_0 = [
                                    {
                                    'type': 'password',
                                    'name': "password_0",
                                    'message': "   Entrez l'ancien mot de passe  :"
                                }
                            ]
            choix_mdp_0 = prompt(element_mdp_0, style=self.style)
            verif = (choix_mdp_0['password_0']==info_client['mdp'])
            
            
            if verif == True :
                element_mdp_1 = [
                                    {
                                        'type': 'password',
                                        'name': 'password_1',
                                        'message': '   Entrer le nouveau mot de passe :'
                                    }
                                ]
                choix_mdp_1 = prompt(element_mdp_1, style=self.style)

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
                                                    'message': '   Mot de passe :'
                                                }
                                            ]
                            choix_mdp_1 = prompt(element_mdp_1, style=self.style)
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
                
                
                if choix_mdp_2["password_2"] != choix_mdp_1["password_1"] :
                    print("Désolé mais les deux mots de passe ne sont pas identiques")
                    return(Modify_information().display_page_change_account(info_client))
                        
                else:
                    
                    ClientAppliClient.modifypassword(info_client['username'],info_client['mdp'],choix_mdp_1["password_1"])
                    info_client['mdp'] = choix_mdp_1["password_1"]
                    print("Le mot de passe a bien été changé")
                    from client.views.profil_page import Home_profile
                    Home_profile().main(info_client)
            else :
                print("le mot de passe actuel n'est pas celui renseigné")
                return(Modify_information().display_page_change_account(info_client))

            

        if (choix_modif2["capital"]=="Modifier adresse") :
            element_num_rue = [
                                {
                                    'type': 'input',
                                    'name': 'adresse_numero_rue',
                                    'message': '   Numero de la rue :',
                                }
                            ]
            choix_num_rue = prompt(element_num_rue, style=self.style)
            #---Retour à lAccueil-----
            if (choix_num_rue["adresse_numero_rue"]=="r") :
                return(Modify_information().display_page_change_account(info_client))

        
            element_rue = [
                            {
                                'type': 'input',
                                'name': 'adresse_rue',
                                'message': '   La Rue :',
                            }
                          ]
            choix_rue = prompt(element_rue, style=self.style)
            #---Retour à lAccueil-----
            if (choix_rue["adresse_rue"]=="r") :
                return(Modify_information().display_page_change_account(info_client))


            
            element_codpostal = [
                            {
                                'type': 'input',
                                'name': 'adresse_code_postal',
                                'message': '   Le code postal :',
                            }
                        ]
            choix_codpostal = prompt(element_codpostal, style=self.style)
            #---Retour à lAccueil-----
            if (choix_codpostal["adresse_code_postal"]=="r") :
                return(Modify_information().display_page_change_account(info_client))
            
            element_ville = [
                                {
                                    'type': 'input',
                                    'name': 'adresse_ville',
                                    'message': '   La Ville :',
                                }
                            ]
            choix_ville = prompt(element_ville, style=self.style)
            #---Retour à lAccueil-----
            if (choix_ville["adresse_ville"]=="r") :
                return(Modify_information().display_page_change_account(info_client))
            
            ###modifier l'adresse
            ClientAppliClient.modifyadress(info_client['username'],mdp = info_client['mdp'],rue = choix_rue['adresse_rue'],codepostal=choix_codpostal['adresse_code_postal'],ville=choix_ville['adresse_ville'],pays = "France")
            print("Votre adresse a bien été changé")
            info_client['adresse']['rue'] = choix_rue['adresse_rue']
            info_client['adresse']['ville'] = choix_ville['adresse_ville']
            info_client['adresse']['codepostal'] = choix_codpostal['adresse_code_postal']
            info_client['adresse']['pays'] = "France"
            from client.views.profil_page import Home_profile
            return Home_profile().main(info_client)
