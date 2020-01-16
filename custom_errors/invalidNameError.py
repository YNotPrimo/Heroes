class InvalidNameError(Exception):
    pass


raise InvalidNameError("Name cannot be less than 2 and more than 50 characters")
