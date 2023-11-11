# -------- package for static part ---------
import time
from PyInquirer import style_from_dict, prompt, Token
from pyfiglet import figlet_format
import pyfiglet


class Home :
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

        self.list_choix_1 = [
                        {
                            'type' : 'list',
                            'name' : 'capital',
                            'message' : ' MENU ACCUEIL ',
                            'choices' : ['Authentification','Créer un compte','QUITTER']
                        }
                    ]

    def aff_first_choiz() :
        style = style_from_dict({
                                        Token.Separator : '#fff',           #white
                                        Token.QuestionMark : '#000',        #black
                                        Token.Selected : '#00BFFF',         #sky blue
                                        Token.Pointer : '#fff',             #white
                                        Token.Instruction : '#fff',         #white
                                        Token.Answer : '#008000 bold',      #green
                                        Token.Question : '#FF7F50',         #shade of orange
                                    })

        list_choix_1 = [
                        {
                            'type' : 'list',
                            'name' : 'capital',
                            'message' : ' MENU ACCUEIL ',
                            'choices' : ['Authentification','Créer un compte','QUITTER']
                        }
                    ]
        choix_1 = prompt(list_choix_1, style=style)
        return choix_1


    # ----------------- DEBUT DE L'APPLICATION ----------------#
    def main(self) :
        print("\n")
        print(" \t \t \t Bienvenue sur")
        Insigne = pyfiglet.figlet_format("E N S A E A T S", font = "slant" )
        print(Insigne)

        print("L'Application de commande qui te permet de délicieux plats en ligne dans \nles meilleurs restaurants proche de vous.")
        print("\n")
        time.sleep(2)

        print("Merci de bien vouloir choisir une Option dans la liste")
        choix = prompt(self.list_choix_1, style=self.style)
        choix_1 = choix["capital"]
        
        if choix_1 =="Authentification":
            from client.views.authentification import Auth
            return Auth().auth()

        if choix_1 =="Créer un compte":
            from client.views.create_compt import class_creation_de_compte
            return class_creation_de_compte().aff_page_create_compt()

        if choix_1 == 'QUITTER':
            print("Merci d'avoir utilisé notre application")
            print("\n \n")
            print(" \t \t \t A bientot sur ")
            Insigne = pyfiglet.figlet_format("E N S A E A T S", font = "slant" )
            print(Insigne)
            return("Vous avez quitté l'application")
