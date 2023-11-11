from PyInquirer import style_from_dict, prompt, Token

class Display_menu:
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

    
    def display_menu(self,list_id_resto, list_resto, info_client, list_menu,idr) :

        
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
            from client.views.display_choices_before_menu import Display_choices_before_menu
            return Display_choices_before_menu().display_choices_before_menu(list_id_resto,list_resto,info_client,list_menu,idr)
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
                Display_menu().display_menu(list_id_resto,list_resto,info_client,list_menu,idr)

                       

        