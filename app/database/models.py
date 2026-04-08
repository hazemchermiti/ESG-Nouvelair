"""
Modèles ORM de la base de données
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database.db import Base


class UserDB(Base):
    """Modèle ORM Utilisateur"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
