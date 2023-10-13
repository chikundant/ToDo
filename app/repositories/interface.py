from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_all(self):
        raise NotImplemented

    @abstractmethod
    def get_by_id(self):
        raise NotImplemented

    @abstractmethod
    def create(self):
        raise NotImplemented

    @abstractmethod
    def update(self):
        raise NotImplemented

    @abstractmethod
    def delete(self):
        raise NotImplemented
