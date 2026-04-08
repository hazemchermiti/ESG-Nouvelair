"""
Modèles utilisateur
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """Base utilisateur"""
    email: EmailStr
    full_name: str
    is_active: bool = True


class UserCreate(UserBase):
    """Création utilisateur"""
    password: str


class UserUpdate(BaseModel):
    """Modification utilisateur"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None


class User(UserBase):
    """Réponse utilisateur"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
