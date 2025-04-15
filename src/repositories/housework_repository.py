import os
import csv
from pathlib import Path

class HouseworkRepository:

    def __init__(self):
        self.data_dir = Path("src/data")
        self.data_dir.mkdir(exist_ok=True)

    def _get_user_file(self, username):
        return self.data_dir / f"{username}_houseworks.csv"

    def get_all(self, username):
        file_path = self._get_user_file(username)
        if not os.path.exists(file_path):
            return []
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]

    def add(self, username, task_name):
        tasks = self.get_all(username)
        if task_name not in tasks:
            tasks.append(task_name)
            self._save_all(username, tasks)

    def delete(self, username, task_name):
        tasks = self.get_all(username)
        if task_name in tasks:
            tasks.remove(task_name)
            self._save_all(username, tasks)

    def update(self, username, old_name, new_name):
        tasks = self.get_all(username)
        tasks = [new_name if task == old_name else task for task in tasks]
        self._save_all(username, tasks)

    def _save_all(self, username, tasks):
        file_path = self._get_user_file(username)
        with open(file_path, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow([task])
