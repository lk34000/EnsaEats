from PyInquirer import style_from_dict, prompt, Token

class Display_choices_before_menu:
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

    
    def display_choices_before_menu(self,list_id_resto, list_resto, info_client, list_menu,idr) :
        liste = ["Voir le menu","Je commande ici","Retour"]
        
        elements_du_menu = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Que voulez vous faire ?:',
                                    'choices' : liste
                                }
                        ]
        

        list_choix = prompt(elements_du_menu, style=self.style)
        choix = list_choix["capital"]

        if(choix=='Retour'):
            from client.views.choice_resto import Choice_resto
            return Choice_resto().resto_near(list_id_resto, list_resto, info_client )
        if(choix=="Voir le menu") : 
            from client.views.display_menu import Display_menu
            return Display_menu().display_menu(list_id_resto,list_resto,info_client,list_menu,idr)
        if(choix == "Je commande ici") :
            from client.api.commande_Client import CommandeAppliClient
            commande = CommandeAppliClient.new_commande(info_client['username'],idr) 
            from client.views.view_order import Display_content_order
            return Display_content_order().create_order(list_id_resto,list_resto,info_client,list_menu,idr,commande)
        
        