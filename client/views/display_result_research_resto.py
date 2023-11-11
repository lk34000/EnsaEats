from PyInquirer import style_from_dict, prompt, Token
from client.api.restaurant_Client import RestaurantAppliClient

class Display_result_research_resto:
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

    
    def view_near_resto(self, info_client) :
        recherche0 = RestaurantAppliClient.get_all_categories(info_client['username'] , info_client['mdp'] )
        if(recherche0[0]!='Retour'):
            recherche0.insert(0,'Retour')
        elements_1 = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Recherche par :',
                                    'choices' : recherche0
                                }
                        ]
        list_choix = prompt(elements_1, style=self.style)
        choix_Desire = list_choix["capital"]
        if(choix_Desire=="Retour"):
            from client.views.search_restaurant import Search_restaurant
            return Search_restaurant().search_restaurant(info_client)
            
        recherche = RestaurantAppliClient.get_restaurant_by_categorie(choix_Desire,info_client['username'] , info_client['mdp'] )

        if recherche == [] : 
            print(" Votre recherche ne comporte aucun restaurant")
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
                from client.views.search_restaurant import Search_restaurant
                return Search_restaurant().search_restaurant(info_client)
        
        result = []
        list_id_resto = []
        for i in range(len(recherche)):
            nom_type = ""
            for type in range(len(recherche[i]['type'])):
                nom_type = nom_type + recherche[i]['type'][type] 

                if (type!=(len(recherche[i]['type'])-1)):
                    nom_type =nom_type + " - "

            result.append(recherche[i]['nom'] + ', ' + nom_type + ", " + recherche[i]['adresse']['rue'] + " " + recherche[i]['adresse']['codepostal'] + " " + recherche[i]['adresse']['ville'] + " Note moyenne : " + str(recherche[i]['notemoyenne']) + "/5")
            list_id_resto.append(recherche[i]['id_restaurant'])

        
        from client.views.choice_resto import Choice_resto
        return Choice_resto().resto_near(list_id_resto , result, info_client)
        
        
        
        


    def view_resto_near_by_desire(self, info_client) :
        list_choix = prompt(self.elements_2, style=self.style)
        choix_desire = list_choix["desire"]
    
        while (choix_desire in ['',' ','  ']) :
            print("Vous n'avez rien entré")

    
            list_choix = prompt(self.elements_2, style=self.style)
            choix_desire = list_choix["desire"]


        if list_choix["desire"] == 'r' :
            from client.views.profil_page import Home_profile
            Home_profile().main(info_client)


        #tester rechercher les resto qui sont autour de lui suivant son envie
        
        recherche = RestaurantAppliClient.get_recherche_restaurant_search(info_client['username'] , info_client['mdp'] ,choix_desire )
        
        #recherche = RestaurantServices.search(exclient, choix_desire)
        result = []
        list_id_resto = []
        if recherche=={'detail': 'Pas de restaurants dans la recherche'} :
            print(" Votre recherche ne comporte aucun restaurant")
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
                from client.views.search_restaurant import Search_restaurant
                return Search_restaurant().search_restaurant(info_client)
                
        for i in range(len(recherche)):
            nom_type = ""
            for type in range(len(recherche[i]['type'])):
                nom_type = nom_type + recherche[i]['type'][type] 

                if (type!=(len(recherche[i]['type'])-1)):
                    nom_type =nom_type + " - "

            result.append(recherche[i]['nom'] + ', ' + nom_type + ", " + recherche[i]['adresse']['rue'] + " " + recherche[i]['adresse']['codepostal'] + " " + recherche[i]['adresse']['ville'] + " Note moyenne : " + str(recherche[i]['notemoyenne']) + "/5")
            list_id_resto.append(recherche[i]['id_restaurant'])


        
        from client.views.choice_resto import Choice_resto
        return Choice_resto().resto_near(list_id_resto , result, info_client)