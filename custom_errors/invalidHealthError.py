class InvalidHealthError(Exception):
    pass


raise InvalidHealthError("Health cannot be less than 0!")
