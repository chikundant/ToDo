from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)

from app.core.settings import settings


class PostgresDBManager:
    def __init__(
        self, url: str = settings.SQLALCHEMY_DATABASE_URI  # type: ignore
    ) -> None:
        self.engine = create_async_engine(
            url,
            pool_pre_ping=True,
        )

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        session: AsyncSession = AsyncSession(self.engine, expire_on_commit=False)

        try:
            async with session:
                yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
