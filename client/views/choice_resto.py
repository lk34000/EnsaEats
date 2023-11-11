from PyInquirer import style_from_dict, prompt, Token

from client.api.menu_Client import MenuAppliClient

class Choice_resto:
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
        

    def resto_near(self,list_id_resto, list_resto, info_client ) :
        if(list_resto[0]!="Retour"):
            list_resto.insert(0, 'Retour')
            
        style = style_from_dict({
                                        Token.Separator : '#fff',           #white
                                        Token.QuestionMark : '#000',        #black
                                        Token.Selected : '#00BFFF',         #sky blue
                                        Token.Pointer : '#fff',             #white
                                        Token.Instruction : '#fff',         #white
                                        Token.Answer : '#008000 bold',      #green
                                        Token.Question : '#FF7F50',         #shade of orange
                                    })

        list_choix = [
                        {
                            'type' : 'list',
                            'name' : 'capital',
                            'message' : ' MENU ACCUEIL ',
                            'choices' : list_resto
                        }
                    ]

        choix = prompt(list_choix, style=style)

        if choix['capital']== 'Retour' :
            from client.views.search_restaurant import Search_restaurant
            return Search_restaurant().search_restaurant(info_client)

        index_choix = list_resto.index(choix['capital'])
        idr = list_id_resto[index_choix - 1]
        #---Menu du restaurant choisie.

        list_menu = MenuAppliClient.get_menus(idr)
        if(len(list_menu)==0) : 
            print("Le restaurant est en maintenance. Veuillez réessayer plus tard.")
            return Choice_resto().resto_near(list_id_resto , list_resto, info_client)
        else :
            from client.views.display_choices_before_menu import Display_choices_before_menu
            return Display_choices_before_menu().display_choices_before_menu(list_id_resto,list_resto,info_client,list_menu,idr)

        


        
