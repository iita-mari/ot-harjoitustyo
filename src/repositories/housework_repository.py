import os
import csv
from pathlib import Path

class HouseworkRepository:
    """
        Repository class for housework-related things.
    """

    def __init__(self):
        """
            Initalializes the HouseworkRepository.

        Args:
            data_dir: Data directory
        """

        self.data_dir = Path("src/data")
        self.data_dir.mkdir(exist_ok=True)

    def _get_user_file(self, username):
        """Get user's file

        Args:
            username: Name of the user

        Returns:
            data_dir: User's data directory
        """

        return self.data_dir / f"{username}_houseworks.csv"

    def get_all(self, username):
        """Get all user's houseworks

        Args:
            username: Name of the user

        Returns:
            string: Returns houseworks from file in string-format
        """

        file_path = self._get_user_file(username)
        if not os.path.exists(file_path):
            return []
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]

    def add(self, username, task_name):
        """Adds housework on user's list/file

        Args:
            username: Name of the user
            task_name: Name of the task (housework)
        """

        tasks = self.get_all(username)
        if task_name not in tasks:
            tasks.append(task_name)
            self._save_all(username, tasks)

    def delete(self, username, task_name):
        """Deletes housework from user's list/file

        Args:
            username: Name of the user
            task_name: Name of the task (housework)
        """

        tasks = self.get_all(username)
        if task_name in tasks:
            tasks.remove(task_name)
            self._save_all(username, tasks)

    def update(self, username, old_name, new_name):
        """Updates housework's name

        Args:
            username: Name of the user
            old_name: Name of the old housework, the housework which name user want's to get changed
            new_name: New name to the housework
        """

        tasks = self.get_all(username)
        tasks = [new_name if task == old_name else task for task in tasks]
        self._save_all(username, tasks)

    def _save_all(self, username, tasks):
        """Saves all houseworkd to user's file

        Args:
            username: User's name
            tasks: Name of the tasks (houseworks)
        """

        file_path = self._get_user_file(username)
        with open(file_path, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow([task])
