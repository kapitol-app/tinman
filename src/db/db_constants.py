class Databases:
    def __init__(self):
        self.kapitol = 'kapitol'

    def is_database_valid(self, db):
        return db == self.kapitol


class Collections:
    def __init__(self):
        self.house = 'house'
        self.senators = 'senators'
        self.legislation = 'legislation'

    def is_collection_valid(self, collection):
        return collection == self.house or collection == self.senators or collection == self.legislation
