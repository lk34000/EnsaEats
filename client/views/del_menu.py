from PyInquirer import style_from_dict, prompt, Token
from client.api.commande_Client import CommandeAppliClient

class Del_menu:
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
    def del_menu(self,list_id_resto, list_resto, info_client, list_menu,idr,commande):
        nom_menu_commande = []
        nom_menu_commande_bis = []
        con = CommandeAppliClient().consult_content(commande['username'],commande['id_restaurant'],commande['date'],commande["contenu"])

        for i in range(len(con)) : 
            if(con[i][0]=="nom") :
                nom_menu_commande.append(con[i][1] + " " + str(con[i+2][1]) + " €")
                nom_menu_commande_bis.append(con[i][1])
        
        nom_menu_commande.append("Retour")
        elements = [
                            {
                                    'type' : 'list',
                                    'name' : 'capital',
                                    'message' : '',
                                    'choices' : nom_menu_commande
                                }
                        ]

        list_choix = prompt(elements, style=self.style)
        choix = list_choix["capital"]

        if(choix=='Retour'):
            from client.views.view_order import Display_content_order
            return Display_content_order().create_order(list_id_resto, list_resto, info_client, list_menu,idr,commande)
        else :
            menu_a_suppr = nom_menu_commande_bis[nom_menu_commande.index(choix)]
            print(menu_a_suppr)
            
            c =CommandeAppliClient.del_menu(menu_a_suppr,commande['username'],commande['id_restaurant'],commande['date'],commande["contenu"])
            print("Le menu " + menu_a_suppr  + " a bien été supprimé de votre commande.")
            from client.views.view_order import Display_content_order
            return Display_content_order().create_order(list_id_resto,list_resto,info_client,list_menu,idr,c)
            
        