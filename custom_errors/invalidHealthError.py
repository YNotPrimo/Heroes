class InvalidHealthError(Exception):
    pass


def msg():
    return "Health cannot be less than 0!"
