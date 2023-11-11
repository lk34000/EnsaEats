from PyInquirer import style_from_dict, prompt, Token
from client.api.client_Client import ClientAppliClient
from client.api.restaurant_Client import RestaurantAppliClient
class View_history:
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
    def view_history(self,info_client):
        hist_com = ClientAppliClient.order_history(info_client['username'],info_client['mdp'])
        liste_res =[]
        if hist_com=='no order for this customer' :
            print("Vous n'avez pas de commande")
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
                from client.views.profil_page import Home_profile
                return Home_profile().main(info_client)

        else :
            
            for c in range(len(hist_com)):
                prix = 0
                for d in range(len(hist_com[c]['contenu'])):
                    prix += hist_com[c]['contenu'][d]['prix']
                

                liste_res.append(hist_com[c]['date'] + " " + RestaurantAppliClient.get_restaurant_by_id(hist_com[c]['id_restaurant'])['nom'] + " : " + str(prix) + " €")
            liste_res.append('Retour')
            elements = [
                                {
                                        'type' : 'list',
                                        'name' : 'capital',
                                        'message' : 'Liste de vos commande:',
                                        'choices' : liste_res
                                    }
                            ]
            list_choix = prompt(elements, style=self.style)
            choix = list_choix["capital"]
            if(choix=='Retour'):
                from client.views.profil_page import Home_profile
                return Home_profile().main(info_client)
            else :
                num_com = hist_com[liste_res.index(choix)]
                from client.views.view_one_order_history import View_one_order
                return View_one_order().view_one_order(info_client,num_com)