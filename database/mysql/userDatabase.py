from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from fastapi_users_db_sqlalchemy import  SQLAlchemyUserDatabase

from app.model.user import User
from app.model.accessToken import AccessToken
from app.dependency.dependency import get_db

from sqlalchemy.ext.asyncio import AsyncSession




async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)



async def get_access_token_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)

if __name__ == '__main__':
    print(get_user_db())
    print(get_access_token_db())