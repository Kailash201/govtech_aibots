class Database:
    ID = 0

    def __init__(self):
        self.id = Database.ID
        Database.ID += 1