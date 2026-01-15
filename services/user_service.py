from models.user import User
from excepts.user_except import UserAlreadyExistsError, UserNotFoundError


class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, user: User):
        if any(u.id == user.id for u in self.users):
            raise UserAlreadyExistsError(f"User with id {user.id} already exists")

        self.users.append(user)
        return user

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                return user
        raise UserNotFoundError(f"User with id {user_id} not found")
