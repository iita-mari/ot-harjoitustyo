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
            "username_taken": if username already exists
            "passwords_dont_match": if passwords don't match
            "success": if user is created
        """

        if self._user_repository.find_by_username(username):
            return "username_taken"
        if password != password2:
            return "passwords_dont_match"
        self._user_repository.create(User(username, password))
        return "success"
