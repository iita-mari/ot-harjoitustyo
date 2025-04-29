import os
import csv
from pathlib import Path

class ContestRepository:
    """
    Repository class for housework-contest related things.
    
    """

    def __init__(self):
        """
        Initalializes the ContestRepository.

        Args:
            data_dir: Data directory
        """

        self.data_dir = Path("src/data")
        self.data_dir.mkdir(exist_ok=True)

    def _get_user_file(self, username):
        """Retrieves a user file by username.

        Args:
            username: Name of the user.

        Returns:
            data.dir: A user's data directory.
        """

        return self.data_dir / f"{username}_contest.csv"

    def load_grid(self, username, task_count):
        """Loads housework grid.

        Args:
            username: Name of the user
            task_count: count of the tasks

        Returns:
            If file exists: returns string
        """

        file_path = self._get_user_file(username)
        if not os.path.exists(file_path):
            return [["" for _ in range(31)] for _ in range(task_count)]
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def save_grid(self, username, grid):
        """Saves housework grid.

        Args:
            username: Name of the user
            grid: Housework grid of the user
        """
        file_path = self._get_user_file(username)
        with open(file_path, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(grid)
