from PyInquirer import style_from_dict, prompt, Token

class View_one_order : 
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
    def view_one_order(self,info_client,com):
        print("Voici le contenu de votre commande : ")
        for c in range(len(com['contenu'])) :
            print(com['contenu'][c]['nom'] + " : " + str(com['contenu'][c]['prix']) + " €")
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
            from client.views.see_history  import View_history
            return View_history().view_history(info_client)