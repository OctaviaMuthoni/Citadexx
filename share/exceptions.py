
# TODO: fully implements DatabaseException class and other Custom Exception classes

class DatabaseExceptions(Exception):
    def __init__(self, message):
        super(DatabaseExceptions, self).__init__(message)



