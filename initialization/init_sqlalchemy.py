from database.mysql.database import engine
from app.model.base import Base
from app.model.user import User
from app.model.accessToken import AccessToken


async def mysql_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)






if __name__ == '__main__':
    from fastapi import Depends
    from app.v1.dependency.dependency import get_user_db
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
    from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase


    def get_user_db(session= Depends(get_user_db)):
        yield SQLAlchemyUserDatabase(session, User)
        session.close()
    print(get_user_db())

    def get_access_token_db(session = Depends(get_user_db)):
        yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
        session.close()
    print(get_access_token_db())