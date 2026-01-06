from models import User
from services import UserService

def main():
    service = UserService()

    user1 = User(1, "Thiago", "thiago@email.com")
    user2 = User(2, "Juan", "juan@email.com")

    service.add_user(user1)
    service.add_user(user2)

    print(service.list_users())

if __name__ == "__main__":
    main()
