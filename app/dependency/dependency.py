from fastapi import Depends
from fastapi_users_db_sqlalchemy import  SQLAlchemyUserDatabase

from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql.database import async_session_maker
from app.model.user import User

from typing import AsyncGenerator




async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


