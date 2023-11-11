from PyInquirer import style_from_dict, prompt, Token

class Home_profile:
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

        self.list_choix_4 = [
                                {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : '',
                                    'choices' : ['Rechercher restaurant','Voir historique des commandes',"Modifier profil",'Déconnection']
                                }
                            ]


    # ----------------- DEBUT DE L'APPLICATION ----------------#
    def main(self, info_client ) :
        print()
        print("Bienvenue "+ info_client['nom'] +" "+info_client['prenom'])
        print()
        #---mettre un message de bien venu----#

        print("Que souhaitez vous faire ?")
        choix_4 = prompt(self.list_choix_4, style=self.style)
        choix_4 = choix_4['capital']
        
        if choix_4 =="Rechercher restaurant":
            from client.views.search_restaurant import Search_restaurant
            return Search_restaurant().search_restaurant(info_client)
            
        if choix_4 =='Voir historique des commandes':
            from client.views.see_history import View_history
            return View_history().view_history(info_client)
        
        
        if choix_4 == 'Modifier profil':
            from client.views.modify_profile import Modify_information
            return Modify_information().display_page_change_account(info_client)
        

        if choix_4 == 'Déconnection':
            from client.views.main import Home
            Home().main()






