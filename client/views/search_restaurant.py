
from PyInquirer import style_from_dict, prompt, Token

class Search_restaurant:
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

        self.list_choix = [
                                {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Recherche par :',
                                    'choices' : ['Liste de toutes les catégories de restaurant autour de vous','Rechercher un nom de restaurant ou une catégorie','Retour']
                                }
                            ]


    # ----------------- DEBUT DE L'APPLICATION ----------------#
    def search_restaurant(self, info_client) :
        choix = prompt(self.list_choix, style=self.style)
        
        choix = choix['capital']
        
        
        if choix =="Liste de toutes les catégories de restaurant autour de vous":
            from client.views.display_result_research_resto import Display_result_research_resto
            return Display_result_research_resto().view_near_resto(info_client)
            

        if choix =="Rechercher un nom de restaurant ou une catégorie":
            from client.views.display_result_research_resto import Display_result_research_resto
            return Display_result_research_resto().view_resto_near_by_desire(info_client)

        if choix == 'Retour':
            from client.views.profil_page import Home_profile
            return Home_profile().main(info_client)


