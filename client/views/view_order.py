from PyInquirer import style_from_dict, prompt, Token
from client.api.commande_Client import CommandeAppliClient
from random import randint

class Display_content_order:
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
        
        self.elements_2 = [
                            {
                                'type': 'input',
                                'name': 'desire',
                                'message': '    De quoi avez-vous envie ? ',
                            }
                        ]
    def create_order(self,list_id_resto, list_resto, info_client, list_menu,idr,commande) :
        print("Composez votre commande : ")
        liste = ["Consulter les menus","Ajoutez un menu","Supprimez un menu","Voir la composition de la commande","Annuler la commande","Valider la commande"]
        elements = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Que voulez vous faire ?:',
                                    'choices' : liste
                                }
                        ]
        

        list_choix = prompt(elements, style=self.style)
        choix = list_choix["capital"]
        if (choix =="Consulter les menus"):
            from client.views.view_menu import View_menu
            return View_menu().consult_menu(list_id_resto,list_resto,info_client,list_menu,idr,commande)

        if(choix == "Annuler la commande") : 
            print("Votre commande a été annulée")
            from client.views.choice_resto import Choice_resto
            return Choice_resto().resto_near(list_id_resto , list_resto, info_client)
        if(choix =="Ajoutez un menu") : 
            from client.views.add_menu import Add_menu
            return Add_menu().add_menu(list_id_resto,list_resto,info_client,list_menu,idr,commande)
        if(choix=="Supprimez un menu") : 
            from client.views.del_menu import Del_menu
            return Del_menu().del_menu(list_id_resto,list_resto,info_client,list_menu,idr,commande)

        if(choix=="Valider la commande") :
            if(commande["contenu"]==[]):
                print("votre commande est vide.")
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
                    return Display_content_order().create_order(list_id_resto,list_resto,info_client,list_menu,idr,commande)
        
            CommandeAppliClient.register_order(commande["username"],commande["id_restaurant"],commande["date"],commande["contenu"],info_client['mdp'])
            print("Votre commande à bien été validée.")
            l = ['Lisa Stofer', 'Mamadou Bamba', 'Tanguy Varet', 'Léon Kourtis', 'Guillaume Pain']
            a = randint(0,4)
            msg = "Vous serez livré par " +  l[a] + " dans " + str(randint(15,30)) + "min."
            print(msg)
            from client.views.profil_page import Home_profile
            return Home_profile().main(info_client)
            


        if(choix == "Voir la composition de la commande"):
            con = CommandeAppliClient().consult_content(commande['username'],commande['id_restaurant'],commande['date'],commande["contenu"])
            pri =CommandeAppliClient().consult_prices(commande['username'],commande['id_restaurant'],commande['date'],commande["contenu"])
            print("Le prix est de " + str(pri) + " €")
            for p in range(len(con)) :
                if(con[p][0]=='nom'):
                    print(con[p][1] +" : " + str(con[p+2][1]) + " €")
            elements = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : '',
                                    'choices' : ['Retour']
                                }
                        ]
            list_choix = prompt(elements, style=self.style)
            choix = list_choix["capital"]
            if(choix=='Retour'):
                return Display_content_order().create_order(list_id_resto,list_resto,info_client,list_menu,idr,commande)
