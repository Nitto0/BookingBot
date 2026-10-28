from config import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models import Base


engine = create_async_engine(DATABASE_URL)
session_maker = async_sessionmaker(engine)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
