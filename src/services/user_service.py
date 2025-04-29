from repositories.user_repository import User, UserRepository

class UserService:
    """Service class for user-related things.
    """

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def authenticate(self, username, password):
        """Authenticates user's loging

        Args:
            username: name of the user
            password: user's password

        Returns:
            user: If user exits and password is correct, returns user
            None: If use does not exit and/or password is incorrect, return None
        """

        user = self._user_repository.find_by_username(username)
        if user and user.password == password:
            return user
        return None

    def create_user(self, username, password, password2):
        """Creates user, if name is not taken and passwords are same

        Args:
            username (_type_): name of the user
            password: password first time
            password2: password second time

        Returns:
            True: If username is taken or username is unique and password matches password2
            False: If passwords are not the same
        """

        if self._user_repository.find_by_username(username):
            return True
        if password != password2:
            return False
        self._user_repository.create(User(username, password))
        return True
