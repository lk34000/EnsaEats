import unittest
from api.services.client_service import Clientservice
from api.Business_Objects.client import Client
from api.Business_Objects.adresse import Adresse
from api.dao.client_dao import ClientDao

class TestClientService(unittest.TestCase):
    def __init__(self, methodName) -> None:
        super().__init__(methodName=methodName)
        self.c = Client(username = "Ballondor", nom = "Dubois", prenom = "Leo",adresse = Adresse(rue = "1 rue de Lyon",ville = "Rennes",codepostal = "35000") , mdp = "olympique")

    def test_newclient(self):
        self.assertEqual(True,Clientservice().nouveauclient(self.c))
    
    def test_authentification_and_get_client1(self):
        #quand l'authentification est validée
        ClientDao().add_client(self.c) #on ajoute le client pour pouvoir tester l'authentification
        self.assertEqual(self.c,Clientservice().authentification_and_get_client(self.c.username,self.c.mdp))
    
    def test_authentification_and_get_client2(self):
        #quand l'authentification n'est pas validée
        fauxclient = Client(username = "Ballondor", nom = "Dubois", prenom = "Leo",adresse = Adresse(rue = "1 rue de Lyon",ville = "Rennes",codepostal = "35000") , mdp = "tropfort")
        self.assertEqual("Cannot authenticate Client "+fauxclient.username,str(Clientservice().authentification_and_get_client(fauxclient.username,fauxclient.mdp)))
    
    def test_username_is_free1(self):
        #quand l'username du client rentré n'est pas dans la base
        fauxclient2 = Client(username = "Nul", nom = "Dubois", prenom = "Leo",adresse = Adresse(rue = "1 rue de Lyon",ville = "Rennes",codepostal = "35000") , mdp = "claquage")
        self.assertEqual(True,Clientservice().usernameisfree(fauxclient2.username))
    
    def test_username_is_free2(self):
        #quand l'username du client rentré est dans la base
        self.assertEqual(False,Clientservice().usernameisfree(self.c.username))
    
    def test_updateclientpassword(self):
        np = "truc"
        self.assertEqual(True,Clientservice().updateclientpassword(self.c.username,np))
    
    def test_updateclientadresse(self):
        adresse = Adresse(rue = "3 rue de Lyon",ville = "Rennes",codepostal = "35000")
        self.assertEqual(True,Clientservice().updateclientadresse(self.c.username,adresse))

    def test_deleteclient(self):
        self.assertEqual(True,Clientservice().deleteclient(self.c.username))

if __name__ == '__main__':
    unittest.main()








