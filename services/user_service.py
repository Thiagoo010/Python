from sqlalchemy.orm import Session
from models.user_models import User
from excepts.user_except import UserAlreadyExistsError, UserNotFoundError

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user):
        exists = self.db.query(User).filter(User.email == user.email).first()
        if exists:
            raise UserAlreadyExistsError("El usuario ya existe")

        new_user = User(
            name=user.name,
            email=user.email
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFoundError("Usuario no encontrado")
        return user
