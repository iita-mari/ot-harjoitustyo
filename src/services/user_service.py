from repositories.user_repository import User, UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def authenticate(self, username, password):
        user = self._user_repository.find_by_username(username)
        if user and user.password == password:
            return user
        return None

    def create_user(self, username, password, password2):
        if self._user_repository.find_by_username(username):
            return True
        if password != password2:
            return False
        self._user_repository.create(User(username, password))
        return True
