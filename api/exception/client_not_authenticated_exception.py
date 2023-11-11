class ClientNotAuthenticated(Exception):
    """Exception raised for errors when you can't authenticate client

    Attributes:
        username -- username of the searched Client
    """

    def __init__(self, username: str):
        self.message = "Cannot authenticate Client "+username 
        super().__init__(self.message)