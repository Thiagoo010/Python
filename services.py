class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def list_users(self):
        return [user.to_dict() for user in self.users]
