class NorestaurantsSearchException(Exception):
     """Exception raised for errors when the search of restaurants returns nothing"""

     def __init__(self):
        self.message = "No restaurant corresponding to the search"
        super().__init__(self.message)


