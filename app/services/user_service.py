"""
Service utilisateur - Logique métier
"""
from sqlalchemy.orm import Session
from app.database.models import UserDB
from app.models import UserCreate, UserUpdate


class UserService:
    """Service pour gérer les utilisateurs"""

    @staticmethod
    def get_user(db: Session, user_id: int):
        """Récupérer un utilisateur par ID"""
        return db.query(UserDB).filter(UserDB.id == user_id).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        """Récupérer un utilisateur par email"""
        return db.query(UserDB).filter(UserDB.email == email).first()

    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100):
        """Récupérer tous les utilisateurs"""
        return db.query(UserDB).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        """Créer un nouvel utilisateur"""
        # En production, utiliser bcrypt pour hasher le password
        db_user = UserDB(
            email=user.email,
            full_name=user.full_name,
            hashed_password=user.password,  # TODO: Hash this
            is_active=user.is_active
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(db: Session, user_id: int, user: UserUpdate):
        """Modifier un utilisateur"""
        db_user = UserService.get_user(db, user_id)
        if not db_user:
            return None
        
        update_data = user.dict(exclude_unset=True)
        for field, value in update_data.items():
            if field == "password":
                setattr(db_user, "hashed_password", value)  # TODO: Hash this
            else:
                setattr(db_user, field, value)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        """Supprimer un utilisateur"""
        db_user = UserService.get_user(db, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user
