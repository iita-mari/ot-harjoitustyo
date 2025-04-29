import os
from pathlib import Path


class User:
    """
        Class for user's name and password.

        Attributes:
            username: User's name
            password: User's password
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserRepository:
    """
        Repository class for user related things.

    """

    def __init__(self, file_path):
        self._file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        Path(self._file_path).touch()

    def _read(self):
        """Reads file where usernames and passwords are saved.

        Returns:
            users: returns list of all users in own rows
        """

        users = []

        with open(self._file_path, "r", encoding='utf-8') as file:
            for row in file:
                row = row.strip()
                if not row:
                    continue
                username, password = row.split(";")
                users.append(User(username, password))
        return users

    def _write(self, users):
        """Writes user's username and password to file

        Args:
            users: User's username and password
        """

        with open(self._file_path, "w", encoding='utf-8') as file:
            for user in users:
                file.write(f"{user.username};{user.password}\n")

    def find_all(self):
        """Reads/finds all written

        Returns:
            read:
        """

        return self._read()

    def find_by_username(self, username):
        """Finds given username from file

        Args:
            username: Name of the user

        Returns:
            User: Returns user
            None: If user is not found, returns None
        """

        for user in self._read():
            if user.username == username:
                return user
        return None

    def create(self, user):
        """Reads user-file and writes user to file

        Args:
            user: New user

        Returns:
            user: Returns new user
        """

        users = self._read()
        users.append(user)
        self._write(users)
        return user
