from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.postgres.postgres import PostgresDBManager
from app.repositories.interface import IRepository
from app.models import Base


class BaseRepository(IRepository):
    model: Base = Base

    def __init__(self, db_manager: PostgresDBManager = PostgresDBManager()):
        self.db_manager: PostgresDBManager = db_manager

    async def create(self, instance: Base) -> Base:
        async with self.db_manager.session() as session:
            session: AsyncSession

            async with session.begin():
                session.add(instance)
                await session.commit()
                return instance

    async def get_by_id(self, pk: str) -> Optional[Base]:
        async with self.db_manager.session() as session:
            session: AsyncSession

            async with session.begin():
                result = await session.execute(
                    select(self.model).where(self.model.id == pk)
                )
                return result.scalars().first()

    async def get_all(self) -> Sequence[Base]:
        async with self.db_manager.session() as session:
            session: AsyncSession

            async with session.begin():
                result = await session.execute(select(self.model))
                return result.scalars().all()

    async def update_account(self, instance: Base) -> Base:
        async with self.db_manager.session() as session:
            session: AsyncSession

            async with session.begin():
                session.add(instance)
                await session.commit()
                return instance

    async def update(self, instance: Base) -> Base:
        async with self.db_manager.session() as session:
            session: AsyncSession

            async with session.begin():
                session.add(instance)
                await session.commit()
                return instance

    async def delete(self, instance: Base) -> Base:
        async with self.db_manager.session() as session:
            session: AsyncSession

            async with session.begin():
                await session.delete(instance)
                await session.commit()
                return instance
