from sqlalchemy import Column, String, Boolean, DateTime, DECIMAL
from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from app.model.base import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    # SQLAlchemyBaseUserTableUUID provides following:
    # ID, Email, hashed_password, is_active, is_superuser, is_verified
    UserName = Column(String(255), nullable=False)
    Phone = Column(String(255), nullable=True)
    UserIcon = Column(String(2048), nullable=True)
    IsDelete = Column(Boolean, default=False)
    JoinTime = Column(DateTime, default=datetime.utcnow)
    LastActivation = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



