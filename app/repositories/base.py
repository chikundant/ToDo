from app.repositories.interface import IRepository


class BaseRepository(IRepository):
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        pass

    def get_by_id(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
