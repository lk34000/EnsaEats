from PyInquirer import style_from_dict, prompt, Token
from client.api.commande_Client import CommandeAppliClient

class Add_menu:
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
    
    def add_menu(self,list_id_resto, list_resto, info_client, list_menu,idr,commande):
        liste = ["Retour"]
        liste_prix=[""]
        for i in range(len(list_menu)):
            liste.append(list_menu[i]["nom"])
            liste_prix.append(list_menu[i]["prix"])
        liste_affichage = []
        for i in range(len(liste)):
            if(i==0):
                liste_affichage.append(liste[i] + " " + str(liste_prix[i]))
            else : 
                liste_affichage.append(liste[i] + " " + str(liste_prix[i])+ " €")
        elements = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : 'Que voulez vous faire ?:',
                                    'choices' : liste_affichage
                                }
                        ]
        list_choix = prompt(elements, style=self.style)
        choix = list_choix["capital"]

        if(choix==liste_affichage[0]):
            from client.views.view_order import Display_content_order
            return Display_content_order().create_order(list_id_resto, list_resto, info_client, list_menu,idr,commande)
        
        menu_choisis = list_menu[liste_affichage.index(choix)-1]
        
        c = CommandeAppliClient.add_menu(menu_choisis['nom'],commande["username"],commande["id_restaurant"],commande["date"],commande["contenu"])
        print("Le menu " + menu_choisis['nom'] + " a bien été ajouté à votre commande.")
        from client.views.view_order import Display_content_order
        return Display_content_order().create_order(list_id_resto,list_resto,info_client,list_menu,idr,c)
        
        