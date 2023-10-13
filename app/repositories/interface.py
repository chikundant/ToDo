from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplemented

    @abstractmethod
    async def get_by_id(self, pk):
        raise NotImplemented

    @abstractmethod
    async def create(self, instance):
        raise NotImplemented

    @abstractmethod
    async def update(self, instance):
        raise NotImplemented

    @abstractmethod
    async def delete(self, instance):
        raise NotImplemented
