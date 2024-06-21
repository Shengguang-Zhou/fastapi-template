from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from app.model.base import Base


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    # SQLAlchemyBaseUserTableUUID provides following:
    # ID, token, create_at
    pass