import os
import csv
from pathlib import Path

class ContestRepository:
    def __init__(self):
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)

    def _get_user_file(self, username):
        return self.data_dir / f"{username}_contest.csv"

    def load_grid(self, username, task_count):
        file_path = self._get_user_file(username)
        if not os.path.exists(file_path):
            return [["" for _ in range(31)] for _ in range(task_count)]
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def save_grid(self, username, grid):
        file_path = self._get_user_file(username)
        with open(file_path, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(grid)
