from PyInquirer import style_from_dict, prompt, Token

class View_menu:
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
        def consult_menu(self,list_id_resto, list_resto, info_client, list_menu,idr,commande):
            print("Voici le menu : ")
            lmen_menu = []
            for i in range(len(list_menu)):
                lmen_menu.append(list_menu[i]["nom"] + " : " + str(list_menu[i]['prix']) + " €")
            lmen_menu.append('Retour')
            elements_du_menu = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Cliquez sur un menu pour voir sa composition ou faire retour:',
                                    'choices' : lmen_menu
                                }
                        ]
        


            list_choix = prompt(elements_du_menu, style=self.style)
            choix = list_choix["capital"]
            if(choix=='Retour'):
                from client.views.view_order import Display_content_order
                return Display_content_order().create_order(list_id_resto,list_resto,info_client,list_menu,idr,commande)
        
        

            else :
                choix_menu = list_menu[lmen_menu.index(choix)]
                print("Voila la composition du menu " + choix_menu['nom'])
                for i in range(len(choix_menu["listplat"])):
                    print(choix_menu["listplat"][i]['nom'])
                elements = [
                    {
                        'type' : 'list',
                        'name' : 'capital',
                        'message' : 'Faire retour:',
                        'choices' : ['Retour']
                                    }
                ]
                list_choix = prompt(elements, style=self.style)
                choix = list_choix["capital"]
                if(choix=='Retour'):
                    View_menu().consult_menu(list_id_resto,list_resto,info_client,list_menu,idr,commande)     