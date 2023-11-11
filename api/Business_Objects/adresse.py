from pydantic.main import BaseModel

class Adresse(BaseModel):
    rue : str
    ville : str
    codepostal : str
    pays : str = 'France'
