class ClientExists(Exception):
    """Exception raised for errors when username already on database

    Attributes:
        username -- username of the searched Client
    """

    def __init__(self, username: str):
        self.message = "Client "+username + " already exists"
        super().__init__(self.message)
