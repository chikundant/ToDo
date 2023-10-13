from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, pk):
        raise NotImplementedError

    @abstractmethod
    async def create(self, instance):
        raise NotImplementedError

    @abstractmethod
    async def update(self, instance):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, instance):
        raise NotImplementedError
