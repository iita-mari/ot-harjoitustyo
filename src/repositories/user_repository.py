import os
from pathlib import Path


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        Path(self._file_path).touch()

    def _read(self):
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
        with open(self._file_path, "w", encoding='utf-8') as file:
            for user in users:
                file.write(f"{user.username};{user.password}\n")

    def find_all(self):
        return self._read()

    def find_by_username(self, username):
        for user in self._read():
            if user.username == username:
                return user
        return None

    def create(self, user):
        users = self._read()
        users.append(user)
        self._write(users)
        return user
