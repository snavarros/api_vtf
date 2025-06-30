from app.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String)
    phone = Column(String)
    region = Column(Integer)
    role = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    provider = Column(String)
