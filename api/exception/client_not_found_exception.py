class ClientNotFoundException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched Client
    """

    def __init__(self, username: str):
        self.message = "Client "+username + " not found"
        super().__init__(self.message)
