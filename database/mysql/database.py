from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Generator

from safety.safety import safety_config


class MYSQLConfig:
    # extract database information
    HOST: str = safety_config.get('mysql', 'mysql_host')
    PORT: int = safety_config.get('mysql', 'mysql_port')
    DB: str = safety_config.get('mysql', 'mysql_database')
    USER: str = safety_config.get('mysql', 'mysql_user')
    PASSWORD: str = safety_config.get('mysql', 'mysql_password')



# engine
DATABASE_URL = f'mysql+asyncmy://{MYSQLConfig.USER}:{MYSQLConfig.PASSWORD}@{MYSQLConfig.HOST}:{MYSQLConfig.PORT}/{MYSQLConfig.DB}'
engine = create_async_engine(DATABASE_URL,
                             echo=True,
                             pool_recycle=3600)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


print('Connected to MySQL')
